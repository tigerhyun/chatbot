# 프로젝트 안내 (Claude용)

이 저장소는 한 사람이 Claude Code로 만들어 가는 개인 프로젝트 모음입니다. 새 세션은 이 파일을 먼저 읽고 이어서 작업합니다.

## 사용자와 소통하는 법

- 사용자는 개발자가 아닙니다. 항상 **한국어로, 쉬운 말로** 설명합니다. 전문 용어는 처음 나올 때 풀어서 씁니다.
- 결과를 말할 때는 무엇을 확인했고 무엇을 확인하지 못했는지 분명히 구분합니다.
- 투자 종목이나 상품을 추천하지 않습니다. 판단을 돕는 도구와 계산을 만듭니다.

## 개인정보 (중요)

- **이 저장소는 공개(public)입니다.** 자산·연봉·회사 이름·가족 정보 같은 사용자의 실제 숫자나 신상은 코드, 문서, 커밋 메시지 어디에도 넣지 않습니다.
- 실제 숫자가 필요한 예시는 누구에게나 해당할 만한 가짜 값을 쓰고, 예시라고 밝힙니다.
- 사용자의 매매·자산 기록은 claude.ai 아티팩트의 비공개 저장소에만 있습니다. Claude도 읽을 수 없습니다.

## 구성

| 경로 | 내용 |
| --- | --- |
| `trading-journal/index.html` | 매매일지 웹앱. claude.ai 아티팩트로 게시됨 |
| `trading-journal/dev/preview.js` | 매매일지를 브라우저로 띄워 문법 확인 + 스크린샷 |
| `chatbot.py` | 터미널에서 Claude와 대화하는 챗봇 (대화는 `conversations/`에 저장, git 제외) |

## 매매일지 앱 (`trading-journal/`)

### 게시
- 게시된 주소: https://claude.ai/artifact/KgvEuswiZHhjmppJ6AjZv9 (사용자만 열 수 있는 비공개 페이지)
- 새 세션에서 고칠 때: Artifact 도구로 위 주소를 먼저 `read`한 뒤, `trading-journal/index.html`을 `url`에 이 주소를 넣어 다시 게시합니다. **주소 없이 게시하면 새 앱이 생겨서 기존 기록이 안 보입니다.**
- 게시된 버전과 저장소 파일이 다르면 게시된 쪽을 기준으로 합치고, 저장소에도 반영합니다.
- 권한(capabilities)은 `{db: {}, user: {}}`입니다. 다시 게시할 때 생략하면 그대로 유지됩니다.

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

### 고친 뒤 확인
```bash
node trading-journal/dev/preview.js            # 문법 확인 + 스크린샷 (scratchpad에 저장)
node trading-journal/dev/preview.js goal       # 특정 탭(open, closed, stats, goal, rules)
```
스크린샷을 직접 보고 겹침·넘침·다크 모드를 확인한 뒤 게시합니다.

## 작업 흐름 (Git)

- `main`이 기준 브랜치입니다. 세션마다 작업 브랜치에서 고치고, 확인이 끝나면 PR을 만들어 `main`에 합칩니다.
- 커밋 메시지는 영어로, 무엇을 왜 바꿨는지 짧게 씁니다.
- 앱을 고쳤다면 게시와 커밋을 함께 합니다. 둘 중 하나만 하면 저장소와 실제 앱이 어긋납니다.

## 관련 문서 (저장소 밖)

- 블로그 연재 기획과 1화 초안: Claude Docs 문서 https://claude.ai/artifact/C3seeAXRXwsAts3fCXM9mj (개인 숫자가 들어 있어 저장소에는 넣지 않음)

## 다음 개선 후보

- [ ] 일부만 매도하기 (지금은 매도하면 전량 처리)
- [ ] 추가 매수 기록 수정·취소
- [ ] 현금흐름 점검표 (월세·이자·생활비 → 저축 여력)
- [ ] 월간 리포트 자동 생성 (블로그 ‘월간 결산’ 초안으로 활용)
- [ ] 매매일지 복기 → 블로그 글 초안 변환
- [ ] 실시간 주가 불러오기 (아티팩트에서 외부 주소 호출이 막혀 있어 방법 검토 필요)
