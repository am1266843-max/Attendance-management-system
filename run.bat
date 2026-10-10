@echo off
setlocal
cd /d "%~dp0"
echo ============================================
echo AI ATTENDANCE MANAGEMENT SYSTEM - GROQ
echo ============================================

if not exist ".env" (
    echo ERROR: .env file not found.
    echo Create .env and add GROQ_API_KEY=your_key
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    echo Creating Python virtual environment...
    py -m venv .venv
    if errorlevel 1 (
        echo Could not create virtual environment. Make sure Python is installed.
        pause
        exit /b 1
    )
)

echo Installing required packages...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo Package installation failed. Check your internet connection and try again.
    pause
    exit /b 1
)

echo Starting attendance system...
".venv\Scripts\python.exe" main.py
pause
