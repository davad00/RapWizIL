#!/bin/bash

echo "Setting up RapWizIL - Hebrew Rap Visualization Tool"
echo ""

# Check if Node.js is installed
echo "[1/4] Checking if Node.js is installed..."
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed. Please install Node.js from https://nodejs.org/"
    exit 1
fi
echo "Node.js is installed ✓"

# Check if Python is installed
echo ""
echo "[2/4] Checking if Python is installed..."
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed. Please install Python 3.8+ from https://python.org/"
        exit 1
    else
        PYTHON_CMD=python
    fi
else
    PYTHON_CMD=python3
fi
echo "Python is installed ✓"

# Install dependencies
echo ""
echo "[3/4] Installing dependencies..."
echo "Installing Node.js dependencies..."
npm install
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Node.js dependencies"
    exit 1
fi

echo "Installing frontend dependencies..."
cd frontend
npm install
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install frontend dependencies"
    exit 1
fi
cd ..

echo "Installing backend dependencies..."
cd backend
$PYTHON_CMD -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install backend dependencies"
    exit 1
fi
cd ..

# Download NLTK data
echo ""
echo "[4/4] Downloading NLTK data..."
cd backend
$PYTHON_CMD -c "import nltk; nltk.download('punkt')"
cd ..

echo ""
echo "============================================"
echo "🎉 Setup completed successfully!"
echo ""
echo "To start the application:"
echo "  npm run dev"
echo ""
echo "The app will be available at:"
echo "  Frontend: http://localhost:3000"
echo "  Backend:  http://localhost:5000"
echo "============================================"
