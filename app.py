from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory user storage
users = {}
next_id = 1

# Seed function
def seed_users():
    global next_id
    initial_users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"}
    ]
    for user in initial_users:
        user['id'] = next_id
        users[next_id] = user
        next_id += 1

seed_users()

# Create user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'id': next_id,
        'name': data['name'],
        'email': data['email']
    }
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

# Read all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

# Read single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = users.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user)

# Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)
