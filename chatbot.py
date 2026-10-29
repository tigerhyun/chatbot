"""터미널에서 Claude와 대화하는 챗봇."""

from datetime import datetime
from pathlib import Path

import anthropic

MODEL = "claude-opus-5-5"
SYSTEM_PROMPT = "당신은 친절한 대화 상대입니다. 사용자가 쓰는 언어로 짧고 자연스럽게 답하세요."
EXIT_WORDS = {"종료", "끝", "quit", "exit", "bye"}
LOG_DIR = Path(__file__).parent / "conversations"


def start_log() -> Path:
    """이번 대화를 저장할 파일을 만든다. 예: conversations/2026-10-29_203300.txt"""
    LOG_DIR.mkdir(exist_ok=True)
    started = datetime.now()
    log_path = LOG_DIR / f"{started:%Y-%m-%d_%H%M%S}.txt"
    log_path.write_text(f"# 대화 시작: {started:%Y-%m-%d %H:%M:%S}\n\n", encoding="utf-8")
    return log_path


def save_line(log_path: Path, speaker: str, text: str) -> None:
    """한 줄씩 바로 덧붙여서, 프로그램이 갑자기 꺼져도 그때까지의 대화는 남게 한다."""
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%H:%M:%S}] {speaker}: {text}\n\n")


def ask_claude(client: anthropic.Anthropic, messages: list) -> str | None:
    """대화 기록을 보내고 답변을 실시간으로 출력한 뒤 기록에 추가한다.

    답변 텍스트를 돌려주고, 거절되면 None을 돌려준다.
    """
    print("🤖 Claude: ", end="", flush=True)
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=64000,
        system=SYSTEM_PROMPT,
        messages=messages,
        output_config={"effort": "low"},
        # 안전 필터가 답변을 거절하면 서버가 추천 모델로 자동 재시도한다.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()
    print()

    if response.stop_reason == "refusal":
        print("(이 질문에는 답할 수 없어요. 다르게 물어봐 주세요.)")
        messages.pop()  # 거절된 질문은 기록에서 뺀다
        return None
    # 텍스트만이 아니라 content 전체를 그대로 기록에 남겨야 다음 요청이 올바르다.
    messages.append({"role": "assistant", "content": response.content})
    return "".join(block.text for block in response.content if block.type == "text")


def main() -> None:
    client = anthropic.Anthropic()  # ANTHROPIC_API_KEY 환경 변수를 사용
    messages = []
    log_path = start_log()
    print("🤖 Claude: 안녕하세요! 대화를 끝내려면 '종료'라고 입력하세요.")
    print(f"(대화 내용은 {log_path} 에 저장돼요.)")
    while True:
        try:
            user_input = input("나: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not user_input:
            continue
        if user_input.lower() in EXIT_WORDS:
            break

        messages.append({"role": "user", "content": user_input})
        save_line(log_path, "나", user_input)
        try:
            reply = ask_claude(client, messages)
            save_line(log_path, "Claude", reply if reply is not None else "(답변 거절됨)")
        except anthropic.AuthenticationError:
            print("\n❌ API 키가 올바르지 않아요. ANTHROPIC_API_KEY를 확인해 주세요.")
            return
        except anthropic.RateLimitError:
            print("\n⏳ 요청이 너무 많아요. 잠시 후 다시 시도해 주세요.")
            messages.pop()
        except anthropic.APIConnectionError:
            print("\n🌐 네트워크 연결을 확인해 주세요.")
            messages.pop()
        except anthropic.APIStatusError as e:
            print(f"\n⚠️ API 오류 ({e.status_code}): {e.message}")
            messages.pop()
    print("🤖 Claude: 안녕히 가세요! 👋")


if __name__ == "__main__":
    main()
