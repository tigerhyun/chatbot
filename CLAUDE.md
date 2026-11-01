@AGENTS.md

# Claude 전용 안내

공용 규칙은 위의 `AGENTS.md`에 있습니다. 여기에는 Claude에서만 해당하는 내용만 둡니다.

## 매매일지 게시
- 세션을 시작하면 `docs/WORKLOG.md`에서 **`게시 필요`** 표시가 남은 기록을 먼저 확인합니다. 있으면 사용자에게 알리고 게시합니다.
- 게시 방법: Artifact 도구로 https://claude.ai/artifact/KgvEuswiZHhjmppJ6AjZv9 를 먼저 `read`한 뒤, `trading-journal/index.html`을 `url`에 이 주소를 넣어 게시합니다. **주소 없이 게시하면 새 앱이 생겨서 기존 기록이 안 보입니다.**
- 게시된 버전과 저장소 파일이 다르면 게시된 쪽을 기준으로 합치고, 저장소에도 반영합니다.
- 권한(capabilities)은 `{db: {}, user: {}}`입니다. 다시 게시할 때 생략하면 그대로 유지됩니다.
- 게시했으면 작업 일지의 해당 `게시 필요`를 `게시 완료`로 바꿉니다.

## 관련 문서 (저장소 밖, Claude 계정에 있음)
- 블로그 연재 기획과 1화 초안: Claude Docs 문서 https://claude.ai/artifact/C3seeAXRXwsAts3fCXM9mj (개인 숫자가 들어 있어 저장소에는 넣지 않음)
