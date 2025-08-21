#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify RapWizIL installation
"""
import sys
import os

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print("[OK] Flask imported successfully")
    except ImportError as e:
        print(f"[ERROR] Flask import failed: {e}")
        return False
    
    try:
        import nltk
        print("[OK] NLTK imported successfully")
    except ImportError as e:
        print(f"[ERROR] NLTK import failed: {e}")
        return False
    
    try:
        from phonikud import PhonemeG2P
        print("[OK] Phonikud imported successfully")
    except ImportError:
        print("[WARNING] Phonikud not available (fallback mode will be used)")
    
    try:
        from backend.hebrew_nlp import HebrewNLPProcessor
        print("[OK] Hebrew NLP processor imported successfully")
    except ImportError as e:
        print(f"[ERROR] Hebrew NLP processor import failed: {e}")
        return False
    
    return True

def test_nlp_processor():
    """Test the Hebrew NLP processor"""
    print("\nTesting Hebrew NLP processor...")
    
    try:
        sys.path.append('backend')
        from hebrew_nlp import HebrewNLPProcessor
        
        processor = HebrewNLPProcessor()
        
        # Test basic functionality
        test_lyrics = """אני רק רוצה להגיד לך איך
שאת יפה כמו שמיים
אני רק רוצה להגיד לך עכשיו
שאת חלמת שלי תמיד"""
        
        result = processor.analyze_lyrics(test_lyrics)
        
        if result and 'lines' in result:
            print("[OK] Hebrew NLP processor working correctly")
            print(f"  - Processed {len(result['lines'])} lines")
            print(f"  - Rhyme scheme: {result.get('rhyme_scheme', 'N/A')}")
            return True
        else:
            print("[ERROR] Hebrew NLP processor returned invalid result")
            return False
            
    except Exception as e:
        print(f"[ERROR] Hebrew NLP processor test failed: {e}")
        return False

def test_backend_startup():
    """Test if the backend can start up"""
    print("\nTesting backend startup...")
    
    try:
        sys.path.append('backend')
        from app import app
        
        # Test if app can be created
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("[OK] Backend startup test successful")
                return True
            else:
                print(f"[ERROR] Backend returned status code: {response.status_code}")
                return False
                
    except Exception as e:
        print(f"[ERROR] Backend startup test failed: {e}")
        return False

def main():
    """Main test function"""
    print("RapWizIL Installation Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_nlp_processor,
        test_backend_startup
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print("-" * 40)
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("[SUCCESS] All tests passed! Installation is working correctly.")
        print("\nYou can now run:")
        print("  npm run dev")
        return True
    else:
        print("[ERROR] Some tests failed. Please check the installation.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
