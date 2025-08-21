#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick test of Hebrew rap analysis with the user's lyrics
"""
import sys
import os

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Add backend to path
sys.path.append('backend')

def test_hebrew_rap():
    """Test the Hebrew NLP with the user's lyrics"""
    try:
        from hebrew_nlp import HebrewNLPProcessor
        
        processor = HebrewNLPProcessor()
        
        # User's lyrics (shortened for testing)
        test_lyrics = """עושה פו על הקנדלז
יש לי יום הולדת
אפס חמש אחד אחד שתיים אפס אפס 
בן 23 כן, עוד מעט בנובמבר
אפס תשע, ארבע שתיים אפס

עושה פו על הקנדלז
יש לי יום הולדת
בן 23 עוד מעט בנובמבר 
אפס חמש אחד אחד שתיים אפס אפס
אפס תשע ארבע שתיים אפס

מחביא תסוד שלי בכספת 
מביעה משאלה עושה פו על הקנדלז
תביא עוגה עם הקצפת
מכין לי חביתה עם בייקון 23 אני לא ברסלב"""
        
        print("Testing Hebrew rap analysis...")
        print("=" * 50)
        
        result = processor.analyze_lyrics(test_lyrics)
        
        if result and 'error' not in result:
            print(f"[OK] Lines processed: {len(result.get('lines', []))}")
            print(f"[OK] Total words: {result.get('statistics', {}).get('total_words', 0)}")
            print(f"[OK] Rhyme scheme: {result.get('rhyme_scheme', 'N/A')}")
            print(f"[OK] Unique rhymes: {result.get('statistics', {}).get('unique_rhymes', 0)}")
            
            # Show rhyme groups
            rhyme_groups = result.get('rhyme_groups', {})
            if rhyme_groups:
                print("\nRhyme groups found:")
                for group, words in rhyme_groups.items():
                    try:
                        print(f"  {group}: {', '.join(words)}")
                    except UnicodeEncodeError:
                        print(f"  {group}: [Hebrew words - {len(words)} words]")
            else:
                print("No rhyme groups detected")
                
            # Show first few lines with rhyme info
            print("\nFirst few lines:")
            for i, line in enumerate(result.get('lines', [])[:5]):
                rhyme_group = line.get('rhyme_group', '-')
                line_text = line.get('text', '')
                try:
                    print(f"  {i+1}. [{rhyme_group}] {line_text}")
                except UnicodeEncodeError:
                    print(f"  {i+1}. [{rhyme_group}] [Hebrew text - {len(line_text)} chars]")
                
            return True
        else:
            print(f"[ERROR] Analysis failed: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_hebrew_rap()
    print("\n" + "=" * 50)
    if success:
        print("[SUCCESS] Hebrew rap analysis improved!")
    else:
        print("[ERROR] Still needs work...")
    
    print("\nRestart the backend to test with the web app:")
    print("  Ctrl+C to stop npm run dev")
    print("  npm run dev")
