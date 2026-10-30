# chatbot

터미널에서 Claude와 대화하는 Python 챗봇입니다. 답변이 실시간으로 출력되고, 이전 대화 내용을 기억합니다.

## 준비

1. [Claude Console](https://platform.claude.com/)에서 API 키를 발급받습니다.
2. 패키지를 설치하고 API 키를 설정합니다.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="발급받은-키"
```

## 실행

```bash
python3 chatbot.py
```

대화를 끝내려면 `종료`(또는 `quit`, `exit`)를 입력하거나 `Ctrl+C`를 누르세요.

## 바꿔 보기

`chatbot.py` 맨 위의 값을 고치면 됩니다.

- `SYSTEM_PROMPT`: 챗봇의 성격과 말투 (예: "해적처럼 말하세요")
- `MODEL`: 사용할 Claude 모델

## 대화 기록

대화할 때마다 `conversations/` 폴더에 `2026-10-29_203300.txt`처럼 시작 시각이 이름인 파일이 생기고, 주고받은 말이 시간과 함께 저장됩니다. 개인적인 내용이 담길 수 있어서 이 폴더는 GitHub에 올라가지 않도록 `.gitignore`에 넣어 두었습니다.

## 블로그 연재

`blog-series/` 폴더에 「블로그 100억 목표 달성기」 연재 계획과 각 화 원고가 있습니다. 계획과 목차는 `blog-series/README.md`, 원고는 `blog-series/posts/`에서 볼 수 있습니다.
