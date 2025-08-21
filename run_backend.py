#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple script to run the backend with proper Python detection
"""
import sys
import os
import subprocess

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

def find_python():
    """Find the correct Python executable"""
    python_commands = ['python', 'python3', 'py']
    
    for cmd in python_commands:
        try:
            result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Found Python: {cmd} - {result.stdout.strip()}")
                return cmd
        except FileNotFoundError:
            continue
    
    print("ERROR: Python not found. Please install Python 3.8+ from https://python.org/")
    sys.exit(1)

def main():
    """Main function to run the backend"""
    # Change to backend directory
    backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
    os.chdir(backend_dir)
    
    # Find Python
    python_cmd = find_python()
    
    # Run the Flask app
    try:
        subprocess.run([python_cmd, 'app.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running backend: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nBackend stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
