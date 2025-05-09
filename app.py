import os
import logging
from typing import Dict, Optional
from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# API Configuration
API_KEY = os.getenv('API_NINJAS_KEY', 'YOUR_API_KEY')  # Get API key from environment variable
API_URL = "https://api.api-ninjas.com/v1/horoscope"

# Zodiac signs data
ZODIAC_SIGNS = {
    'aries': 'March 21 - April 19',
    'taurus': 'April 20 - May 20',
    'gemini': 'May 21 - June 20',
    'cancer': 'June 21 - July 22',
    'leo': 'July 23 - August 22',
    'virgo': 'August 23 - September 22',
    'libra': 'September 23 - October 22',
    'scorpio': 'October 23 - November 21',
    'sagittarius': 'November 22 - December 21',
    'capricorn': 'December 22 - January 19',
    'aquarius': 'January 20 - February 18',
    'pisces': 'February 19 - March 20'
}

# Zodiac characteristics
ZODIAC_TRAITS = {
    'aries': {
        'personality': 'Bold, ambitious, and confident',
        'thoughts': 'Always thinking about new challenges and adventures'
    },
    'taurus': {
        'personality': 'Reliable, patient, and practical',
        'thoughts': 'Focused on stability and enjoying life\'s pleasures'
    },
    'gemini': {
        'personality': 'Adaptable, curious, and communicative',
        'thoughts': 'Constantly processing new information and ideas'
    },
    'cancer': {
        'personality': 'Intuitive, emotional, and protective',
        'thoughts': 'Deeply concerned with home, family, and emotional security'
    },
    'leo': {
        'personality': 'Dramatic, creative, and confident',
        'thoughts': 'Thinking about leadership, recognition, and creative expression'
    },
    'virgo': {
        'personality': 'Analytical, practical, and detail-oriented',
        'thoughts': 'Focused on improvement, organization, and helping others'
    },
    'libra': {
        'personality': 'Diplomatic, gracious, and fair-minded',
        'thoughts': 'Always seeking balance, harmony, and meaningful relationships'
    },
    'scorpio': {
        'personality': 'Passionate, resourceful, and determined',
        'thoughts': 'Deeply analyzing situations and seeking truth'
    },
    'sagittarius': {
        'personality': 'Optimistic, adventurous, and philosophical',
        'thoughts': 'Contemplating big ideas and future possibilities'
    },
    'capricorn': {
        'personality': 'Disciplined, responsible, and ambitious',
        'thoughts': 'Planning for long-term success and stability'
    },
    'aquarius': {
        'personality': 'Progressive, original, and independent',
        'thoughts': 'Thinking about innovation and making the world better'
    },
    'pisces': {
        'personality': 'Compassionate, artistic, and intuitive',
        'thoughts': 'Immersed in creative and spiritual contemplation'
    }
}

def test_api_connection():
    """Test the API connection and print the response."""
    try:
        logger.info("Testing API connection...")
        response = requests.get(
            f"{API_URL}?zodiac=aries",
            headers={'X-Api-Key': API_KEY}
        )
        logger.info(f"Test API Response Status: {response.status_code}")
        logger.info(f"Test API Response Headers: {response.headers}")
        logger.info(f"Test API Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        logger.error(f"API Test Error: {str(e)}")
        return False

def get_horoscope(zodiac: str) -> Optional[Dict]:
    """Get horoscope data for the given zodiac sign."""
    try:
        logger.info(f"Fetching horoscope for {zodiac}")
        response = requests.get(
            f"{API_URL}?zodiac={zodiac}",
            headers={'X-Api-Key': API_KEY}
        )
        logger.info(f"API Response Status: {response.status_code}")
        logger.info(f"API Response: {response.text}")
        
        if response.status_code == 401:
            logger.error("API key authentication failed")
            return None
            
        response.raise_for_status()
        data = response.json()
        
        if not data:
            logger.error("Empty response from API")
            return None
            
        # Add zodiac traits to the response
        data['traits'] = ZODIAC_TRAITS.get(zodiac.lower(), {
            'personality': 'Unknown',
            'thoughts': 'Unknown'
        })
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching horoscope: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"Response content: {e.response.text}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html', zodiac_signs=ZODIAC_SIGNS)

@app.route('/get_horoscope', methods=['POST'])
def get_horoscope_route() -> Dict:
    """Handle horoscope lookup request."""
    try:
        zodiac = request.form.get('zodiac', '').strip().lower()
        logger.info(f"Received request for zodiac sign: {zodiac}")
        
        if not zodiac:
            return jsonify({'error': 'Please select a zodiac sign'}), 400

        if zodiac not in ZODIAC_SIGNS:
            return jsonify({'error': 'Invalid zodiac sign'}), 400

        horoscope_data = get_horoscope(zodiac)
        if not horoscope_data:
            return jsonify({'error': 'Failed to fetch horoscope data. Please try again later.'}), 500

        return jsonify({
            'zodiac': zodiac.capitalize(),
            'date_range': ZODIAC_SIGNS[zodiac],
            'horoscope': horoscope_data.get('horoscope', ''),
            'traits': horoscope_data.get('traits', {
                'personality': 'Unknown',
                'thoughts': 'Unknown'
            })
        }), 200

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check() -> Dict:
    """Health check endpoint."""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    if API_KEY == 'YOUR_API_KEY':
        logger.warning("Please set your API_NINJAS_KEY in the .env file")
    else:
        # Test API connection on startup
        if test_api_connection():
            logger.info("API connection test successful")
        else:
            logger.error("API connection test failed")
    logger.info("Starting Flask application...")
    app.run(debug=True, port=5001) 