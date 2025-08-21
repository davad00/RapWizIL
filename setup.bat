@echo off
echo Setting up RapWizIL - Hebrew Rap Visualization Tool
echo.

echo [1/4] Checking if Node.js is installed...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed. Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)
echo Node.js is installed ✓

echo.
echo [2/4] Checking if Python is installed...
python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python is not installed. Please install Python 3.8+ from https://python.org/
        pause
        exit /b 1
    ) else (
        echo Python is installed (using 'py' command) ✓
        set PYTHON_CMD=py
    )
) else (
    echo Python is installed ✓
    set PYTHON_CMD=python
)

echo.
echo [3/4] Installing dependencies...
echo Installing Node.js dependencies...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install Node.js dependencies
    pause
    exit /b 1
)

echo Installing frontend dependencies...
cd frontend
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install frontend dependencies
    pause
    exit /b 1
)
cd ..

echo Installing backend dependencies...
cd backend
%PYTHON_CMD% -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install backend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo [4/4] Downloading NLTK data...
cd backend
%PYTHON_CMD% -c "import nltk; nltk.download('punkt')"
cd ..

echo.
echo ============================================
echo 🎉 Setup completed successfully!
echo.
echo To start the application:
echo   npm run dev
echo.
echo The app will be available at:
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:5000
echo ============================================
pause
