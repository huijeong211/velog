import feedparser
import git
import os
import re

# [수정 1] 올바른 벨로그 RSS 피드 URL (v2.velog.io 사용)
rss_url = 'https://v2.velog.io/rss/@huijeong211'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# 깃 커밋용 사용자 설정
with repo.config_writer() as git_config:
    git_config.set_value('user', 'name', 'github-actions[bot]')
    git_config.set_value('user', 'email', 'github-actions[bot]@users.noreply.github.com')

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

new_posts_added = False

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # [수정 2] 파일명으로 사용할 수 없는 특수문자 제거
    file_name = entry.title
    file_name = re.sub(r'[\\/*?:"<>|]', '-', file_name) + '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        # [수정 3] description 대신 content/summary/description 순으로 본문 긁어오기
        content = ''
        if hasattr(entry, 'content'):
            content = entry.content[0].value
        elif hasattr(entry, 'summary'):
            content = entry.summary
        elif hasattr(entry, 'description'):
            content = entry.description

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        # 깃 스테이징 및 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')
        new_posts_added = True

# [수정 4] 새 포스팅이 커밋되었다면 깃허브 원격 저장소로 Push
if new_posts_added:
    origin = repo.remote(name='origin')
    origin.push()
    print("Successfully pushed new posts to GitHub!")
else:
    print("No new posts to update.")
