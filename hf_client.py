import json

from groq import Groq

from .config import GROQ_API_KEY, GROQ_MODEL


SYSTEM_PROMPT = """
You are an attendance-management command parser.

Your ONLY job is to convert the user's natural-language attendance request
into JSON.

Return ONLY valid JSON. Do not use markdown fences. Do not explain anything.

Allowed actions:
1. check_attendance
2. mark_attendance
3. remove_attendance
4. student_percentage
5. class_average
6. all_percentages

Required JSON shape:
{
  \"action\": \"...\",
  \"student\": \"student name or roll number or null\",
  \"date\": \"YYYY-MM-DD or null\"
}

Rules:
- For check_attendance, mark_attendance, remove_attendance:
  student and date are required.
- For student_percentage:
  student is required and date is null.
- For class_average and all_percentages:
  student and date are null.
- Interpret dates in the project range as 8 Oct 2026 through 14 Oct 2026.
- \"mark\", \"present\", \"add attendance\" means mark_attendance.
- \"remove\", \"absent\", \"unmark\" means remove_attendance.
- \"was ... present\" means check_attendance.
- Never calculate percentages yourself.
- Never invent a student name or roll number.
"""


def get_client() -> Groq:
    if not GROQ_API_KEY or GROQ_API_KEY == "PASTE_YOUR_GROQ_API_KEY_HERE":
        raise RuntimeError(
            "GROQ_API_KEY is missing. Open the .env file and paste your Groq API key."
        )
    return Groq(api_key=GROQ_API_KEY)


def parse_command(user_text: str) -> dict:
    client = get_client()

    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text},
        ],
        temperature=0,
        max_tokens=200,
        response_format={"type": "json_object"},
    )

    content = (completion.choices[0].message.content or "").strip()
    try:
        result = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Groq returned invalid JSON: {content}") from exc

    required = {"action", "student", "date"}
    if set(result.keys()) != required:
        raise ValueError("AI response must contain exactly: action, student, date.")

    allowed_actions = {
        "check_attendance",
        "mark_attendance",
        "remove_attendance",
        "student_percentage",
        "class_average",
        "all_percentages",
    }
    if result["action"] not in allowed_actions:
        raise ValueError(f"Unsupported action: {result['action']}")

    return result
