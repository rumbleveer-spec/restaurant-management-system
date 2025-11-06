"""
Restaurant Management System - Backend API
Author: Ankit Rajput
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key-change-in-production')

# Enable CORS
CORS(app)

# Initialize JWT
jwt = JWTManager(app)

# Import routes
from routes import auth, menu, inventory, orders, recipes

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(menu.bp)
app.register_blueprint(inventory.bp)
app.register_blueprint(orders.bp)
app.register_blueprint(recipes.bp)

@app.route('/')
def index():
    return jsonify({
        'message': 'Restaurant Management System API',
        'author': 'Ankit Rajput',
        'version': '1.0.0',
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
