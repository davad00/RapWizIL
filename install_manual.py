#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manual installation script for RapWizIL
This script directly installs requirements without fancy output
"""
import sys
import subprocess
import os

def install_packages():
    """Install packages directly"""
    packages = [
        "Flask>=3.0.0",
        "Flask-CORS>=4.0.0", 
        "requests>=2.32.3",
        "nltk>=3.9.1",
        "flask-limiter>=3.8.0",
        "python-dotenv>=1.0.1",
        "gunicorn>=21.2.0"
    ]
    
    print("Installing basic packages...")
    for package in packages:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True, capture_output=True)
            print(f"Installed: {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
    
    # Try NumPy
    print("Installing NumPy...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "numpy"], check=True, capture_output=True)
        print("Installed: numpy")
    except subprocess.CalledProcessError:
        print("NumPy installation failed - trying alternative...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "--only-binary=all", "numpy"], check=True, capture_output=True)
            print("Installed: numpy (binary)")
        except subprocess.CalledProcessError:
            print("Warning: Could not install NumPy")
    
    # Try Phonikud (optional)
    print("Installing Phonikud (optional)...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "phonikud"], check=True, capture_output=True)
        print("Installed: phonikud")
    except subprocess.CalledProcessError:
        print("Warning: Phonikud not available - will use fallback mode")
    
    # Download NLTK data
    print("Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        print("Downloaded NLTK data")
    except Exception as e:
        print(f"Warning: NLTK data download failed: {e}")

if __name__ == "__main__":
    print(f"Using Python: {sys.executable}")
    print(f"Version: {sys.version}")
    install_packages()
    print("\nInstallation completed!")
    print("Run: py run_backend.py (or python run_backend.py)")
    print("Then: npm run dev:frontend")
