# RapWizIL Troubleshooting Guide

## Common Installation Issues

### 1. Python Not Found

**Error:** `Python was not found; run without arguments to install from the Microsoft Store`

**Solutions:**
- **Option A:** Install Python from [python.org](https://python.org) (recommended)
- **Option B:** Install from Microsoft Store
- **Option C:** Use the Windows Python Launcher: `py` instead of `python`

**Test your Python installation:**
```bash
python --version
# or
py --version
```

### 2. NumPy Installation Failed (Python 3.12+)

**Error:** `AttributeError: module 'pkgutil' has no attribute 'ImpImporter'`

**Solutions:**
1. **Update pip first:**
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Use our custom installer:**
   ```bash
   npm run install:backend
   ```

3. **Manual installation (if needed):**
   ```bash
   python -m pip install numpy>=1.26.0
   python -m pip install -r backend/requirements.txt
   ```

### 3. React Development Server Error

**Error:** `Invalid options object. Dev Server has been initialized using an options object`

**Solution:**
This is fixed in the latest version. Make sure you have the latest frontend configuration:

```bash
cd frontend
npm install
```

### 4. Phonikud Not Available

**Warning:** `Phonikud not available. Using fallback Hebrew processing.`

**Impact:** The app will still work but with simplified Hebrew rhyme detection.

**Solutions:**
1. **Try installing Phonikud manually:**
   ```bash
   pip install phonikud
   ```

2. **If that fails, the app will use fallback mode automatically**

### 5. NLTK Data Missing

**Error:** `LookupError: Resource punkt not found`

**Solution:**
```bash
python -c "import nltk; nltk.download('punkt')"
```

Or use our installer:
```bash
npm run install:backend
```

## Installation Verification

Test your installation:
```bash
npm test
```

This will verify:
- ✅ All Python dependencies
- ✅ Hebrew NLP processor
- ✅ Backend startup
- ✅ Frontend build capability

## Development Issues

### Backend Won't Start

1. **Check Python path:**
   ```bash
   # Try these commands:
   python run_backend.py
   py run_backend.py
   python backend/app.py
   ```

2. **Check dependencies:**
   ```bash
   python -c "import flask; print('Flask OK')"
   ```

3. **Check port conflicts:**
   - Make sure port 5000 is not in use
   - Try changing the port in `backend/app.py`

### Frontend Issues

1. **Port already in use:**
   ```bash
   # Kill process on port 3000 (Windows)
   netstat -ano | findstr :3000
   taskkill /PID <PID> /F
   
   # Or change port in package.json
   "start": "PORT=3001 react-scripts start"
   ```

2. **Missing dependencies:**
   ```bash
   cd frontend
   rm -rf node_modules
   npm install
   ```

## Platform-Specific Issues

### Windows

1. **Use Git Bash or PowerShell** (not Command Prompt)
2. **Python executable names:**
   - Try `py` instead of `python`
   - Try `python3` instead of `python`

### macOS/Linux

1. **Python version:**
   ```bash
   python3 --version
   which python3
   ```

2. **Permission issues:**
   ```bash
   sudo chmod +x setup.sh
   ./setup.sh
   ```

## API Issues

### Backend API Not Responding

1. **Check if backend is running:**
   ```bash
   curl http://localhost:5000/health
   ```

2. **Check logs:**
   - Look at terminal output when running backend

3. **CORS issues:**
   - Make sure Flask-CORS is installed
   - Check browser developer console

### Analysis Not Working

1. **Test with simple Hebrew text:**
   ```
   שלום עולם
   טוב מאוד
   ```

2. **Check Hebrew text encoding:**
   - Make sure text is in UTF-8
   - No mixed languages in input

## Performance Issues

### Slow Analysis

1. **Large text input:**
   - Break into smaller chunks
   - Limit to ~50 lines at a time

2. **Memory usage:**
   - Restart backend if memory usage is high

### Frontend Slow

1. **Development vs Production:**
   ```bash
   # For production build:
   npm run build
   ```

2. **Browser cache:**
   - Clear browser cache
   - Try incognito/private mode

## Getting Help

If none of these solutions work:

1. **Check the error logs** in your terminal
2. **Run the test suite:** `npm test`
3. **Try a clean installation:**
   ```bash
   rm -rf node_modules frontend/node_modules
   npm run install:all
   ```

4. **Create an issue** with:
   - Your operating system
   - Python version (`python --version`)
   - Node.js version (`node --version`)
   - Full error message
   - Steps to reproduce

## Quick Reset

If everything is broken, try this complete reset:

```bash
# Clean everything
rm -rf node_modules frontend/node_modules

# Reinstall everything
npm run install:all

# Test installation
npm test

# Start the app
npm run dev
```

This should resolve most common issues!
