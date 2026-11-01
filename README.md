# 개인 프로젝트 모음

Claude Code로 만들고 고쳐 나가는 개인 프로젝트입니다. `main` 브랜치가 최신 버전입니다.

| 프로젝트 | 설명 | 위치 |
| --- | --- | --- |
| 나의 매매일지 | 원칙 체크리스트로 충동 매수를 막고, 매매를 복기하고, 자산과 목표를 기록하는 웹앱 | [`trading-journal/`](trading-journal/) |
| 터미널 챗봇 | 터미널에서 Claude와 대화하는 Python 챗봇 | [`chatbot.py`](chatbot.py) |

## 나의 매매일지

claude.ai 아티팩트로 게시되어 휴대폰에서도 열 수 있습니다. 기록은 각자의 claude.ai 계정 안에 비공개로 저장되고, 이 저장소에는 앱 코드만 있습니다.

- **보유 중**: 매수 기록, 추가 매수(평균 매수가 자동 계산), 수정, 현재가 입력
- **매매 기록**: 매도와 복기, 계획대로 팔았는지 표시
- **통계·복기**: 승률, 손익비, 원칙 준수 vs 위반 성과, 기분별 성과, 물타기 성과
- **목표·자산**: 월별 자산 그래프, 목표 시뮬레이터(수익률별 도달 시기)
- **내 원칙**: 매수 전 체크리스트, 비중·손실 한도

화면 확인용 스크립트:

```bash
node trading-journal/dev/preview.js goal   # 문법 확인 + 스크린샷 (예시 데이터)
```

## 터미널 챗봇

답변이 실시간으로 출력되고, 이전 대화 내용을 기억합니다.

1. [Claude Console](https://platform.claude.com/)에서 API 키를 발급받습니다.
2. 패키지를 설치하고 API 키를 설정한 뒤 실행합니다.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="발급받은-키"
python3 chatbot.py
```

대화를 끝내려면 `종료`(또는 `quit`, `exit`)를 입력하거나 `Ctrl+C`를 누르세요.

- `chatbot.py` 맨 위의 `SYSTEM_PROMPT`(성격과 말투), `MODEL`(Claude 모델)을 고쳐 바꿀 수 있습니다.
- 대화는 `conversations/` 폴더에 시작 시각 이름의 파일로 저장됩니다. 개인적인 내용이 담길 수 있어 GitHub에는 올라가지 않습니다.

## 작업 방식

새 기능은 작업 브랜치에서 만들고, 확인한 뒤 Pull Request로 `main`에 합칩니다. Claude가 이어서 작업할 때 참고하는 안내는 [`CLAUDE.md`](CLAUDE.md)에 있습니다.
