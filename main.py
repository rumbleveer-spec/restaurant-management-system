"""
Restaurant Management System - Backend API
Author: Ankit Rajput
Description: Flask backend for restaurant management with JWT authentication
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import jwt
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
CORS(app)

# Demo user database (replace with actual database in production)
users = {
    'admin': {
        'password': 'admin123',
        'role': 'admin'
    }
}

# In-memory storage (replace with PostgreSQL in production)
menu_items = []
inventory_items = []
orders = []
recipes = []

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = token.split(' ')[1]  # Remove 'Bearer ' prefix
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['username']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# Auth Routes
@app.route('/api/auth/login', methods=['POST'])
def login():
    """User login endpoint"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password:
        token = jwt.encode({
            'username': username,
            'role': users[username]['role'],
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({
            'token': token,
            'username': username,
            'role': users[username]['role']
        }), 200

    return jsonify({'message': 'Invalid credentials!'}), 401

# Menu Routes
@app.route('/api/menu-items', methods=['GET'])
@token_required
def get_menu_items(current_user):
    """Get all menu items"""
    return jsonify({'data': menu_items}), 200

@app.route('/api/menu-items', methods=['POST'])
@token_required
def create_menu_item(current_user):
    """Create new menu item"""
    data = request.get_json()
    data['id'] = len(menu_items) + 1
    data['created_at'] = datetime.utcnow().isoformat()
    menu_items.append(data)
    return jsonify({'data': data}), 201

@app.route('/api/menu-items/<int:item_id>', methods=['PUT'])
@token_required
def update_menu_item(current_user, item_id):
    """Update menu item"""
    data = request.get_json()
    for item in menu_items:
        if item['id'] == item_id:
            item.update(data)
            return jsonify({'data': item}), 200
    return jsonify({'message': 'Item not found'}), 404

@app.route('/api/menu-items/<int:item_id>', methods=['DELETE'])
@token_required
def delete_menu_item(current_user, item_id):
    """Delete menu item"""
    global menu_items
    menu_items = [item for item in menu_items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

# Inventory Routes
@app.route('/api/inventory', methods=['GET'])
@token_required
def get_inventory(current_user):
    """Get all inventory items"""
    return jsonify({'data': inventory_items}), 200

@app.route('/api/inventory', methods=['POST'])
@token_required
def create_inventory_item(current_user):
    """Add inventory item"""
    data = request.get_json()
    data['id'] = len(inventory_items) + 1
    data['created_at'] = datetime.utcnow().isoformat()
    inventory_items.append(data)
    return jsonify({'data': data}), 201

# Order Routes
@app.route('/api/orders', methods=['GET'])
@token_required
def get_orders(current_user):
    """Get all orders"""
    return jsonify({'data': orders}), 200

@app.route('/api/orders', methods=['POST'])
@token_required
def create_order(current_user):
    """Create new order"""
    data = request.get_json()
    data['id'] = len(orders) + 1
    data['status'] = 'pending'
    data['created_at'] = datetime.utcnow().isoformat()
    orders.append(data)
    return jsonify({'data': data}), 201

# Recipe Routes
@app.route('/api/recipes', methods=['GET'])
@token_required
def get_recipes(current_user):
    """Get all recipes"""
    return jsonify({'data': recipes}), 200

@app.route('/api/recipes', methods=['POST'])
@token_required
def create_recipe(current_user):
    """Create new recipe"""
    data = request.get_json()
    data['id'] = len(recipes) + 1
    data['created_at'] = datetime.utcnow().isoformat()
    recipes.append(data)
    return jsonify({'data': data}), 201

# Health check
@app.route('/health', methods=['GET'])
def health_check():
    """API health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'author': 'Ankit Rajput'
    }), 200

if __name__ == '__main__':
    print('\n' + '='*60)
    print('🍽️  Restaurant Management System - Backend API')
    print('👨‍💻 Author: Ankit Rajput')
    print('🚀 Server starting on http://localhost:5000')
    print('='*60 + '\n')
    app.run(debug=True, host='0.0.0.0', port=5000)
