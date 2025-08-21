import re
import logging
from typing import List, Dict, Tuple, Set
from collections import defaultdict, Counter
import nltk
from nltk.tokenize import word_tokenize

# Try to import phonikud, fall back to basic Hebrew processing if not available
try:
    from phonikud import PhonemeG2P
    PHONIKUD_AVAILABLE = True
except ImportError:
    print("Warning: Phonikud not available. Using fallback Hebrew processing.")
    PHONIKUD_AVAILABLE = False
    PhonemeG2P = None

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

logger = logging.getLogger(__name__)

class HebrewNLPProcessor:
    """
    Hebrew NLP processor for rap lyrics analysis
    Handles tokenization, phonetic transcription, and rhyme detection
    """
    
    def __init__(self):
        """Initialize the Hebrew NLP processor"""
        if PHONIKUD_AVAILABLE:
            try:
                self.g2p = PhonemeG2P()
                logger.info("Hebrew G2P model loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load G2P model: {e}")
                self.g2p = None
        else:
            logger.warning("Phonikud not available, using fallback Hebrew processing")
            self.g2p = None
        
        # Hebrew text preprocessing patterns
        self.hebrew_pattern = re.compile(r'[א-ת]+')
        self.punctuation_pattern = re.compile(r'[^\w\s]', re.UNICODE)
        
        # Reduced stop words list - keep more words for better rhyme detection in rap
        self.stop_words = {
            'את', 'של', 'על', 'אל', 'לא', 'או', 'גם', 'כי', 'אם', 'עם'
        }
    
    def test_connection(self) -> bool:
        """Test if the processor is working correctly"""
        try:
            test_word = "שלום"
            if self.g2p:
                phonemes = self.g2p(test_word)
                return len(phonemes) > 0
            return False
        except Exception as e:
            logger.error(f"Test connection failed: {e}")
            return False
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess Hebrew text for analysis
        
        Args:
            text: Raw Hebrew text
            
        Returns:
            Cleaned and normalized text
        """
        # Split into lines first
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove tabs and excessive whitespace at start/end
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Keep Hebrew letters, spaces, and common punctuation
            # Allow numbers in Hebrew text (they're often part of lyrics)
            cleaned_line = re.sub(r'[^\u0590-\u05FF\s0-9.,!?׃־]', ' ', line)
            
            # Clean up multiple spaces
            cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()
            
            # Only add non-empty lines with Hebrew content
            if cleaned_line and re.search(r'[\u0590-\u05FF]', cleaned_line):
                cleaned_lines.append(cleaned_line)
        
        return '\n'.join(cleaned_lines)
    
    def extract_hebrew_words(self, text: str) -> List[str]:
        """
        Extract Hebrew words from text
        
        Args:
            text: Hebrew text
            
        Returns:
            List of Hebrew words
        """
        words = []
        for word in text.split():
            # Check if word contains Hebrew characters
            if self.hebrew_pattern.search(word):
                # Extract only the Hebrew part
                hebrew_match = self.hebrew_pattern.search(word)
                if hebrew_match:
                    hebrew_word = hebrew_match.group()
                    if len(hebrew_word) > 1:  # Ignore single character words
                        words.append(hebrew_word)
        return words
    
    def get_phonetic_transcription(self, word: str) -> str:
        """
        Get phonetic transcription of a Hebrew word
        
        Args:
            word: Hebrew word
            
        Returns:
            Phonetic transcription
        """
        if not self.g2p:
            # Fallback: use simplified Hebrew phonetic approximation
            return self._simple_hebrew_phonetic(word)
        
        try:
            phonemes = self.g2p(word)
            if phonemes:
                return ' '.join(phonemes)
            return self._simple_hebrew_phonetic(word)
        except Exception as e:
            logger.warning(f"Failed to get phonetic transcription for '{word}': {e}")
            return self._simple_hebrew_phonetic(word)
    
    def _simple_hebrew_phonetic(self, word: str) -> str:
        """
        Improved Hebrew phonetic approximation when Phonikud is not available
        
        Args:
            word: Hebrew word
            
        Returns:
            Simplified phonetic representation focused on endings for rhymes
        """
        # Enhanced Hebrew letter to sound mapping for better rhyme detection
        mapping = {
            'א': 'a', 'ב': 'b', 'ג': 'g', 'ד': 'd', 'ה': 'h', 'ו': 'u',
            'ז': 'z', 'ח': 'ch', 'ט': 't', 'י': 'i', 'כ': 'k', 'ך': 'k',
            'ל': 'l', 'מ': 'm', 'ם': 'm', 'נ': 'n', 'ן': 'n', 'ס': 's',
            'ע': 'a', 'פ': 'p', 'ף': 'f', 'צ': 'ts', 'ץ': 'ts', 'ק': 'k',
            'ר': 'r', 'ש': 'sh', 'ת': 't'
        }
        
        # Handle common Hebrew endings and transformations
        word = word.lower()
        
        # Convert numbers to Hebrew sounds (common in rap)
        word = re.sub(r'23', 'esrim ve shalosh', word)
        word = re.sub(r'\d+', 'num', word)  # Replace other numbers
        
        # Convert Hebrew letters to phonetic representation
        phonetic = ''.join(mapping.get(char, char) for char in word)
        
        # For rhyme detection, focus on suffix patterns
        if len(phonetic) >= 4:
            return phonetic[-4:]  # Last 4 characters for better rhyme matching
        elif len(phonetic) >= 2:
            return phonetic[-2:]  # At least 2 characters
        return phonetic
    
    def calculate_phonetic_similarity(self, word1_phonetic: str, word2_phonetic: str) -> float:
        """
        Calculate phonetic similarity between two words with improved Hebrew rhyme detection
        
        Args:
            word1_phonetic: Phonetic transcription of first word
            word2_phonetic: Phonetic transcription of second word
            
        Returns:
            Similarity score (0.0 - 1.0)
        """
        if word1_phonetic == word2_phonetic:
            return 1.0
        
        # For our simplified phonetic system, treat as character strings
        if not word1_phonetic or not word2_phonetic:
            return 0.0
        
        # Direct suffix comparison for better rhyme detection
        min_len = min(len(word1_phonetic), len(word2_phonetic))
        
        # Count matching characters from the end
        suffix_matches = 0
        for i in range(1, min_len + 1):
            if word1_phonetic[-i] == word2_phonetic[-i]:
                suffix_matches += 1
            else:
                break
        
        # Calculate similarity - be more generous with Hebrew rhymes
        if suffix_matches >= 2:  # At least 2 matching ending characters
            suffix_ratio = suffix_matches / min_len
            return min(1.0, suffix_ratio * 1.2)  # Boost rhyme scores
        elif suffix_matches == 1 and min_len <= 3:  # Short words, 1 match is okay
            return 0.6
        
        # Check for partial matches (less strict)
        if word1_phonetic[-1] == word2_phonetic[-1]:  # Same ending sound
            return 0.5
        
        # Special Hebrew rhyming patterns
        # Check for common Hebrew endings that often rhyme
        common_endings = [
            ('et', 'at'), ('im', 'am'), ('ot', 'ut'), 
            ('tz', 'z'), ('ch', 'k'), ('sh', 's')
        ]
        
        for end1, end2 in common_endings:
            if (word1_phonetic.endswith(end1) and word2_phonetic.endswith(end2)) or \
               (word1_phonetic.endswith(end2) and word2_phonetic.endswith(end1)):
                return 0.5
        
        return 0.0
    
    def detect_rhymes(self, words_with_phonetics: List[Tuple[str, str]]) -> Dict[str, int]:
        """
        Detect rhyme groups in a list of words with improved Hebrew sensitivity
        
        Args:
            words_with_phonetics: List of (word, phonetic) tuples
            
        Returns:
            Dictionary mapping words to rhyme group IDs
        """
        if not words_with_phonetics:
            return {}
        
        rhyme_groups = {}
        rhyme_group_id = 0
        similarity_threshold = 0.4  # Lower threshold for Hebrew rhymes
        
        for i, (word1, phonetic1) in enumerate(words_with_phonetics):
            if word1 in rhyme_groups:
                continue
                
            # Start a new rhyme group
            current_group = rhyme_group_id
            rhyme_groups[word1] = current_group
            group_has_members = False
            
            # Find other words that rhyme with this one
            for j, (word2, phonetic2) in enumerate(words_with_phonetics[i + 1:], i + 1):
                if word2 in rhyme_groups:
                    continue
                    
                similarity = self.calculate_phonetic_similarity(phonetic1, phonetic2)
                if similarity >= similarity_threshold:
                    rhyme_groups[word2] = current_group
                    group_has_members = True
            
            # Only increment group ID if this group has multiple members
            if group_has_members:
                rhyme_group_id += 1
            else:
                # Remove single-word groups (no rhymes found)
                del rhyme_groups[word1]
        
        return rhyme_groups
    
    def analyze_lyrics(self, lyrics: str) -> Dict:
        """
        Analyze Hebrew rap lyrics for rhyme schemes and patterns
        
        Args:
            lyrics: Hebrew rap lyrics text
            
        Returns:
            Analysis results including rhyme schemes, groups, and statistics
        """
        try:
            # Preprocess the text
            cleaned_lyrics = self.preprocess_text(lyrics)
            lines = [line.strip() for line in cleaned_lyrics.split('\n') if line.strip()]
            
            if not lines:
                return {
                    "error": "No valid Hebrew text found in lyrics"
                }
            
            analysis_result = {
                "lines": [],
                "rhyme_scheme": "",
                "rhyme_groups": {},
                "statistics": {
                    "total_lines": len(lines),
                    "total_words": 0,
                    "unique_rhymes": 0
                }
            }
            
            all_line_words = []
            line_end_words = []
            
            # Process each line
            for line_idx, line in enumerate(lines):
                words = self.extract_hebrew_words(line)
                
                if not words:
                    analysis_result["lines"].append({
                        "line_number": line_idx + 1,
                        "text": line,
                        "words": [],
                        "end_word": None
                    })
                    continue
                
                # Get phonetic transcriptions for all words
                words_with_phonetics = []
                for word in words:
                    if word not in self.stop_words:  # Skip common words
                        phonetic = self.get_phonetic_transcription(word)
                        words_with_phonetics.append((word, phonetic))
                
                # The last word in the line is typically the rhyming word
                end_word = words[-1] if words else None
                if end_word and end_word not in self.stop_words:
                    end_phonetic = self.get_phonetic_transcription(end_word)
                    line_end_words.append((end_word, end_phonetic, line_idx))
                
                analysis_result["lines"].append({
                    "line_number": line_idx + 1,
                    "text": line,
                    "words": [
                        {
                            "text": word,
                            "phonetic": phonetic
                        } for word, phonetic in words_with_phonetics
                    ],
                    "end_word": {
                        "text": end_word,
                        "phonetic": self.get_phonetic_transcription(end_word) if end_word else None
                    } if end_word else None
                })
                
                all_line_words.extend(words_with_phonetics)
            
            # Detect rhymes among line-ending words
            if line_end_words:
                end_words_only = [(word, phonetic) for word, phonetic, _ in line_end_words]
                rhyme_groups = self.detect_rhymes(end_words_only)
                
                # Map rhyme groups back to lines
                rhyme_scheme_letters = []
                rhyme_letter_map = {}
                current_letter = 'A'
                
                for word, phonetic, line_idx in line_end_words:
                    if word in rhyme_groups:
                        group_id = rhyme_groups[word]
                        if group_id not in rhyme_letter_map:
                            rhyme_letter_map[group_id] = current_letter
                            current_letter = chr(ord(current_letter) + 1)
                        rhyme_scheme_letters.append(rhyme_letter_map[group_id])
                        
                        # Add rhyme group info to the line
                        if line_idx < len(analysis_result["lines"]):
                            analysis_result["lines"][line_idx]["rhyme_group"] = rhyme_letter_map[group_id]
                    else:
                        rhyme_scheme_letters.append('-')
                        if line_idx < len(analysis_result["lines"]):
                            analysis_result["lines"][line_idx]["rhyme_group"] = '-'
                
                analysis_result["rhyme_scheme"] = ''.join(rhyme_scheme_letters)
                analysis_result["rhyme_groups"] = {
                    letter: [word for word, group_id in rhyme_groups.items() 
                            if rhyme_letter_map.get(group_id) == letter]
                    for letter in rhyme_letter_map.values()
                }
            
            # Calculate statistics
            analysis_result["statistics"]["total_words"] = len(all_line_words)
            analysis_result["statistics"]["unique_rhymes"] = len(set(analysis_result["rhyme_groups"].keys()))
            
            return analysis_result
            
        except Exception as e:
            logger.error(f"Error in analyze_lyrics: {e}")
            return {
                "error": f"Analysis failed: {str(e)}"
            }
