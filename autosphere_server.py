#!/usr/bin/env python3
"""
AutoSphere AI - Flask Server
Combines frontend serving with backend AI functionality
"""

import os
import json
import logging
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from autosphere_ai import AutoSphereAI

# Load environment variables
load_dotenv('config.env')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, static_folder='.')
CORS(app, origins=os.getenv('ALLOWED_ORIGINS', 'http://localhost:8000').split(','))

# Global AI instance
ai_instance = None

def initialize_ai():
    """Initialize the AutoSphere AI instance"""
    global ai_instance
    try:
        # Get credentials from environment variables
        api_key = os.getenv('IBM_API_KEY')
        project_id = os.getenv('IBM_PROJECT_ID')
        
        if not api_key or not project_id:
            logger.error("Missing IBM API credentials in config.env")
            return False
            
        # Initialize AI instance
        ai_instance = AutoSphereAI(api_key, project_id)
        logger.info("AutoSphere AI initialized successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize AI: {str(e)}")
        return False

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, etc.)"""
    return send_from_directory('.', filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests from frontend"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        conversation_history = data.get('conversation_history', [])
        
        if not message:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        if not ai_instance:
            return jsonify({
                'success': False,
                'error': 'AI service not initialized'
            }), 503
        
        # Process the message with conversation history
        response = ai_instance.process_message(message, conversation_history)
        
        return jsonify({
            'success': True,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'ai_initialized': ai_instance is not None,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    """Clear conversation history"""
    try:
        # This could be extended to clear server-side conversation storage
        return jsonify({
            'success': True,
            'message': 'Conversation cleared'
        })
    except Exception as e:
        logger.error(f"Clear conversation error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Failed to clear conversation'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

def main():
    """Main function to run the server"""
    # Initialize AI
    if not initialize_ai():
        logger.warning("Starting server without AI functionality")
    
    # Get server configuration
    host = os.getenv('HOST', 'localhost')
    port = int(os.getenv('PORT', 8000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting AutoSphere AI Server on {host}:{port}")
    logger.info(f"Frontend available at: http://{host}:{port}")
    logger.info(f"API endpoints available at: http://{host}:{port}/api/")
    
    # Run the server
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )

if __name__ == "__main__":
    main()
