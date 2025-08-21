from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv
import logging
from hebrew_nlp import HebrewNLPProcessor

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Rate limiting
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
limiter.init_app(app)

# Initialize Hebrew NLP processor
nlp_processor = HebrewNLPProcessor()

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "RapWizIL Hebrew Rap Visualization API",
        "version": "1.0.0"
    })

@app.route('/analyze', methods=['POST'])
@limiter.limit("10 per minute")
def analyze_lyrics():
    """
    Analyze Hebrew rap lyrics for rhyme schemes and patterns
    
    Expected input:
    {
        "lyrics": "Hebrew rap lyrics text here"
    }
    
    Returns:
    {
        "success": True,
        "data": {
            "lines": [...],
            "rhyme_scheme": "AABB",
            "rhyme_groups": {...},
            "statistics": {...}
        }
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'lyrics' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'lyrics' field in request body"
            }), 400
        
        lyrics = data['lyrics'].strip()
        
        if not lyrics:
            return jsonify({
                "success": False,
                "error": "Lyrics cannot be empty"
            }), 400
        
        # Process the Hebrew lyrics
        logger.info(f"Processing lyrics with {len(lyrics)} characters")
        analysis_result = nlp_processor.analyze_lyrics(lyrics)
        
        return jsonify({
            "success": True,
            "data": analysis_result
        })
        
    except Exception as e:
        logger.error(f"Error analyzing lyrics: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Internal server error occurred while analyzing lyrics"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Detailed health check"""
    try:
        # Test NLP processor
        test_result = nlp_processor.test_connection()
        
        return jsonify({
            "status": "healthy",
            "components": {
                "nlp_processor": "ready" if test_result else "error"
            }
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    logger.info(f"Starting RapWizIL API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
