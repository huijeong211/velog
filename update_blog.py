import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@huijeong211'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# --- [여기 3줄 추가] 깃 커밋용 사용자 설정 ---
with repo.config_writer() as git_config:
    git_config.set_value('user', 'name', 'github-actions[bot]')
    git_config.set_value('user', 'email', 'github-actions[bot]@users.noreply.github.com')

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title
    file_name = file_name.replace('/', '-').replace('\\', '-')
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)

        # 깃허브 커밋 (이제 정상 작동함!)
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')
