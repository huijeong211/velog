# 📝 Velog Automatic Sync & Tech Log

벨로그([@huijeong211](https://velog.io/@huijeong211))에 작성하는 개인 기술 블로그 포스팅을 **GitHub Actions**를 통해 매일 자동으로 동기화하는 저장소입니다.

CS 기초, 리눅스/시스템 하위 레벨 동작 원리, 네트워크, 보안(Dreamhack) 학습 내용을 기록하고 복습합니다.

---

## 🛠️ Auto Sync Architecture

- **Source:** Velog RSS Feed (`https://api.velog.io/rss/@huijeong211`)
- **Automation:** GitHub Actions (`.github/workflows/`)
- **Schedule:** 매일 00:00 UTC (한국 시간 오전 09:00) 자동 수집 및 커밋
- **Script:** Python (`feedparser`, `GitPython`) 기반 새 포스팅 감지 및 Markdown 저장

---

## 📂 Directory Structure

```text
.
├── .github/workflows/   # GitHub Actions 자동화 워크플로우
├── velog-posts/         # 자동 동기화된 벨로그 마크다운(.md) 파일 저장소
├── update_blog.py       # RSS 파싱 및 Git 커밋 스크립트
└── README.md            # 저장소 안내 문서
