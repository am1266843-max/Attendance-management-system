# AI Attendance Management System (Groq)

## Quick start on Windows
1. Install Python 3.10 or newer.
2. Open `.env` in Notepad or VS Code. Replace `PASTE_YOUR_GROQ_API_KEY_HERE` with your Groq API key. Keep the model line as it is unless you choose another model available in your Groq console.
3. Double-click `run.bat`. It creates a virtual environment, installs the dependencies, and starts the terminal application.

You can also open PowerShell in this folder and run `run.bat`.

## Example commands
- `Was Aarav Sharma present on 10 Oct 2026?`
- `Was roll 101 present on 8 Oct 2026?`
- `Mark Priya Verma present on 9 Oct 2026`
- `Remove Rahul Kumar attendance on 11 Oct 2026`
- `What is Aarav Sharma's attendance percentage?`
- `Show all attendance percentages`
- `What is the class attendance average?`

Type `help` for examples and `exit` to quit. Attendance data is stored in `json/students.json`; the latest response is written to `outputs/last_response.json`. Python performs calculations and updates the JSON data. The AI only interprets the natural-language command.

## Notes
- Your API key stays in `.env`; do not share or publish it.
- Groq free usage has rate limits and can change. An API key does not guarantee unlimited usage.
