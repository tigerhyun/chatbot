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
