#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backend installation script with better Python compatibility handling
"""
import sys
import os
import subprocess
import platform

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"ERROR: Python {version.major}.{version.minor} is not supported.")
        print("Please install Python 3.8 or later from https://python.org/")
        return False
    
    print(f"[OK] Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_requirements():
    """Install Python requirements with compatibility handling"""
    backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
    requirements_path = os.path.join(backend_dir, 'requirements.txt')
    
    if not os.path.exists(requirements_path):
        print(f"ERROR: Requirements file not found at {requirements_path}")
        return False
    
    print("Installing Python dependencies...")
    
    # For Python 3.12+, we might need to install some packages differently
    version = sys.version_info
    if version.major == 3 and version.minor >= 12:
        print("Detected Python 3.12+, using compatible installation method...")
        
        # Install packages one by one to handle compatibility issues
        packages = [
            "Flask>=3.0.0",
            "Flask-CORS>=4.0.0", 
            "requests>=2.32.3",
            "nltk>=3.9.1",
            "flask-limiter>=3.8.0",
            "python-dotenv>=1.0.1",
            "gunicorn>=21.2.0"
        ]
        
        # Try to install numpy separately first
        try:
            print("Installing NumPy...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
            subprocess.run([sys.executable, "-m", "pip", "install", "numpy>=1.26.0"], check=True)
            print("[OK] NumPy installed successfully")
        except subprocess.CalledProcessError:
            print("Warning: NumPy installation failed, trying alternative...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "numpy"], check=True)
                print("[OK] NumPy installed with alternative method")
            except subprocess.CalledProcessError:
                print("ERROR: Could not install NumPy. You may need to install it manually.")
                return False
        
        # Try to install phonikud
        try:
            print("Installing Phonikud...")
            subprocess.run([sys.executable, "-m", "pip", "install", "phonikud"], check=True)
            print("[OK] Phonikud installed successfully")
        except subprocess.CalledProcessError:
            print("Warning: Phonikud installation failed. The app will work with reduced functionality.")
        
        # Install other packages
        for package in packages:
            try:
                print(f"Installing {package}...")
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            except subprocess.CalledProcessError:
                print(f"Warning: Failed to install {package}")
    else:
        # Standard installation for older Python versions
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
        except subprocess.CalledProcessError:
            print("Standard installation failed, trying alternative method...")
            return False
    
    print("[OK] Backend dependencies installed successfully")
    return True

def download_nltk_data():
    """Download required NLTK data"""
    print("Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)  # For newer NLTK versions
        print("[OK] NLTK data downloaded successfully")
        return True
    except Exception as e:
        print(f"Warning: NLTK data download failed: {e}")
        return False

def main():
    """Main installation function"""
    print("Installing RapWizIL Backend Dependencies")
    print("=" * 50)
    
    if not check_python_version():
        sys.exit(1)
    
    if not install_requirements():
        print("[ERROR] Installation failed")
        sys.exit(1)
    
    download_nltk_data()
    
    print("\n" + "=" * 50)
    print("[SUCCESS] Backend installation completed!")
    print("\nTo start the backend:")
    print("  python run_backend.py")
    print("\nOr to start both frontend and backend:")
    print("  npm run dev")

if __name__ == "__main__":
    main()
