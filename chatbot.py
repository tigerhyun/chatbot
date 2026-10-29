"""터미널에서 대화하는 간단한 규칙 기반 챗봇."""

import random
from datetime import datetime

EXIT_WORDS = {"종료", "끝", "quit", "exit", "bye"}

# (키워드 목록, 가능한 답변 목록)
RULES = [
    (["안녕", "hello", "hi", "하이"], ["안녕하세요! 반가워요 😊", "안녕! 오늘 기분은 어때요?"]),
    (["이름", "누구"], ["저는 파이썬으로 만든 간단한 챗봇이에요."]),
    (["기분", "어때"], ["저는 언제나 좋아요! 당신은요?"]),
    (["고마", "감사", "thank"], ["천만에요!", "도움이 됐다니 기뻐요."]),
    (["심심", "놀자"], ["저랑 이야기해요! 좋아하는 게 뭐예요?"]),
    (["좋아", "행복"], ["와, 좋네요! 😄"]),
    (["슬퍼", "우울", "힘들"], ["많이 힘드셨겠어요. 이야기 들어줄게요."]),
]

FALLBACKS = [
    "흥미롭네요! 조금 더 이야기해 줄래요?",
    "음, 잘 이해하지 못했어요. 다르게 말해 줄래요?",
    "그렇군요. 그래서요?",
]


def get_response(message: str) -> str:
    text = message.strip().lower()
    if not text:
        return "무슨 말이든 해 주세요!"
    if "시간" in text or "몇 시" in text:
        return f"지금은 {datetime.now():%H시 %M분}이에요."
    if "날짜" in text or "오늘" in text:
        return f"오늘은 {datetime.now():%Y년 %m월 %d일}이에요."
    for keywords, answers in RULES:
        if any(keyword in text for keyword in keywords):
            return random.choice(answers)
    return random.choice(FALLBACKS)


def main() -> None:
    print("🤖 챗봇: 안녕하세요! 대화를 끝내려면 '종료'라고 입력하세요.")
    while True:
        try:
            message = input("나: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if message.strip().lower() in EXIT_WORDS:
            break
        print(f"🤖 챗봇: {get_response(message)}")
    print("🤖 챗봇: 안녕히 가세요! 👋")


if __name__ == "__main__":
    main()
