# 프로젝트 안내 (AI 코딩 도구 공용)

이 저장소는 한 사람이 여러 AI 코딩 도구(Claude Code, ChatGPT Codex, Cursor 등)를 번갈아 쓰며 만들어 가는 개인 프로젝트 모음입니다. **GitHub의 `main` 브랜치가 유일한 기준**이고, 어떤 도구로 작업하든 이 파일을 먼저 읽고 이어서 작업합니다.

## 사용자와 소통하는 법

- 사용자는 개발자가 아닙니다. 항상 **한국어로, 쉬운 말로** 설명합니다. 전문 용어는 처음 나올 때 풀어서 씁니다.
- 결과를 말할 때는 무엇을 확인했고 무엇을 확인하지 못했는지 분명히 구분합니다.
- 투자 종목이나 상품을 추천하지 않습니다. 판단을 돕는 도구와 계산을 만듭니다.

## 여러 AI를 번갈아 쓸 때의 규칙

1. **시작할 때**: `main`의 최신 상태에서 시작하고, 이 파일과 [`docs/WORKLOG.md`](docs/WORKLOG.md)의 최근 기록을 읽습니다. 앞선 도구가 남긴 "다음 할 일"과 "게시 필요" 표시를 확인합니다.
2. **작업 중**: 작업 브랜치에서 고칩니다. `main`에 직접 커밋하지 않습니다.
3. **끝날 때**: `docs/WORKLOG.md` 맨 위에 기록을 하나 추가하고(날짜, 사용한 도구, 한 일, 확인한 것, 다음 할 일), PR을 만들어 `main`에 합칩니다.
4. **한 번에 한 도구만**: 두 도구가 동시에 같은 파일을 고치면 충돌이 납니다. 앞선 작업이 `main`에 합쳐진 뒤 다음 도구를 씁니다.
5. **도구 전용 기능에 기대지 않기**: 특정 AI에서만 되는 기능을 쓸 때는 이 파일에 그 사실과 대안을 적습니다. (현재 하나 있음: 아래 ‘게시’)
6. 이 파일은 모든 도구가 함께 씁니다. 규칙을 바꾸면 여기에 반영하고, 도구별 파일(`CLAUDE.md` 등)에는 그 도구에만 해당하는 내용만 둡니다.

## 개인정보 (중요)

- **이 저장소는 공개(public)입니다.** 자산·연봉·회사 이름·가족 정보 같은 사용자의 실제 숫자나 신상은 코드, 문서, 커밋 메시지, 작업 일지 어디에도 넣지 않습니다.
- 실제 숫자가 필요한 예시는 누구에게나 해당할 만한 가짜 값을 쓰고, 예시라고 밝힙니다.
- 사용자의 매매·자산 기록은 claude.ai 아티팩트의 비공개 저장소에만 있습니다. 어떤 AI도 읽을 수 없습니다.

## 구성

| 경로 | 내용 |
| --- | --- |
| `trading-journal/index.html` | 매매일지 웹앱 (HTML 파일 하나, 외부 빌드 없음) |
| `trading-journal/dev/preview.js` | 매매일지를 브라우저로 띄워 문법 확인 + 스크린샷 |
| `chatbot.py` | 터미널에서 Claude와 대화하는 챗봇 (대화는 `conversations/`에 저장, git 제외) |
| `docs/WORKLOG.md` | 도구를 바꿔도 이어서 일할 수 있게 남기는 작업 일지 |

## 매매일지 앱 (`trading-journal/`)

### 게시 — 지금은 Claude에서만 가능
- 앱은 claude.ai 아티팩트로 게시되어 있습니다: https://claude.ai/artifact/KgvEuswiZHhjmppJ6AjZv9 (사용자만 열 수 있는 비공개 페이지)
- 기록 저장도 claude.ai의 저장 기능(`window.claude.use("db")`, `use("user")`)을 씁니다. 그래서 **코드는 어떤 도구로든 고칠 수 있지만, 실제 앱에 반영(게시)하는 것은 Claude 세션에서만 됩니다.**
- Claude가 아닌 도구로 앱을 고쳤다면: 작업 일지에 **`게시 필요`** 라고 남기고 사용자에게 알려 주세요. 사용자는 Claude에게 "최신 main으로 매매일지 게시해줘"라고 하면 됩니다.
- 이 의존을 없애려면 앱을 다른 곳(예: GitHub Pages)에 올리고 저장 방식을 바꿔야 합니다. 기존 기록을 옮기는 문제가 있어 아직 하지 않았습니다.

### 데이터 구조 (바꿀 때 주의)
모든 기록은 각 사용자의 비공개 공간 `data/users/<uid>/` 아래에 있습니다. 이미 쌓인 기록이 있으므로 **필드 이름을 바꾸거나 지우지 말고, 새 필드는 없을 때도 동작하게** 추가합니다.

- `settings` (문서): `rules[]`, `capital`, `maxWeight`, `maxLossPct`, `goal`, `currentAssets`, `sim{total, invest, monthly, saveGrowth, rate, otherGrowth, age, years}`
- `journal/trades/<id>`: `name, buyDate, buyPrice(평균 매수가), qty, target, stop, reason, emotion, horizon, checks{}, violations[], warnings[], status('open'|'closed'), createdAt, currentPrice?, sellDate?, sellPrice?, sellReason?, review?, edits[]?, originalPlan?, adds[]?, initialBuy?`
- `journal/assets/<YYYY-MM>`: `month, total, invest, memo, savedAt`

### 앱의 원칙 (기능을 더할 때도 지킵니다)
- 기록은 지우지 않고 흔적을 남깁니다. 계획 수정, 손절가 하향, 물타기, 원칙 위반은 표시가 남습니다.
- 원칙을 어기는 행동은 막지 않되, 본인이 직접 확인란에 체크해야 저장됩니다.
- 상승은 빨강, 하락은 파랑(국내 시장 관례). 색은 `:root` 토큰으로만 쓰고 다크 모드도 함께 맞춥니다.
- 금액은 원화 기준, 표시는 `won()` / `short()` 함수를 씁니다.
- 외부 스크립트는 cdnjs 등 허용된 CDN에서 정확한 버전으로만 불러옵니다. 그 밖의 외부 주소 호출(주가 API 등)은 게시 환경에서 막힙니다.

### 고친 뒤 확인
```bash
node trading-journal/dev/preview.js            # 문법 확인 + 스크린샷
node trading-journal/dev/preview.js goal       # 특정 탭(open, closed, stats, goal, rules)
```
- Playwright가 없으면 먼저 설치합니다: `npm i playwright && npx playwright install chromium`
- 스크린샷을 직접 보고 겹침·넘침·다크 모드를 확인합니다.

## Git 규칙

- 기준 브랜치는 `main`. 작업 브랜치 → PR → `main`.
- 커밋 메시지는 영어로, 무엇을 왜 바꿨는지 짧게 씁니다.
- 앱을 고쳤다면 게시까지 해야 끝입니다. 게시를 못 했다면 작업 일지에 `게시 필요`를 남깁니다.

## 다음 개선 후보

- [ ] 일부만 매도하기 (지금은 매도하면 전량 처리)
- [ ] 추가 매수 기록 수정·취소
- [ ] 현금흐름 점검표 (월세·이자·생활비 → 저축 여력)
- [ ] 월간 리포트 자동 생성 (블로그 ‘월간 결산’ 초안으로 활용)
- [ ] 매매일지 복기 → 블로그 글 초안 변환
- [ ] 실시간 주가 불러오기 (게시 환경에서 외부 주소 호출이 막혀 있어 방법 검토 필요)
- [ ] 앱을 claude.ai 밖에서도 열 수 있게 옮기기 (위 ‘게시’ 참고)
