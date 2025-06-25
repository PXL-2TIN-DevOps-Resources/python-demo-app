from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app, template_file=None, config={
    'headers': [],
    'specs': [
        {
            'endpoint': 'swagger',
            'route': '/swagger.json',
            'rule_filter': lambda rule: True,
            'model_filter': lambda tag: True,
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/'  # This changes the docs URL to /
})

# In-memory user storage
users = {}
next_id = 1

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

@app.route('/users', methods=['POST'])
@swag_from({
    'tags': ['Users'],
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'email': {'type': 'string'}
            },
            'required': ['name', 'email']
        }
    }],
    'responses': {
        201: {'description': 'User created'},
        400: {'description': 'Invalid input'}
    }
})
def create_user():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    user = {'id': next_id, 'name': data['name'], 'email': data['email']}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'responses': {
        200: {'description': 'List of users'}
    }
})
def get_users():
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'parameters': [{
        'name': 'user_id',
        'in': 'path',
        'type': 'integer',
        'required': True
    }],
    'responses': {
        200: {'description': 'User data'},
        404: {'description': 'User not found'}
    }
})
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
@swag_from({
    'tags': ['Users'],
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'in': 'body', 'name': 'body', 'required': True,
         'schema': {
             'type': 'object',
             'properties': {
                 'name': {'type': 'string'},
                 'email': {'type': 'string'}
             }
         }}
    ],
    'responses': {
        200: {'description': 'User updated'},
        400: {'description': 'Invalid input'},
        404: {'description': 'User not found'}
    }
})
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

@app.route('/users/<int:user_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Users'],
    'parameters': [{
        'name': 'user_id',
        'in': 'path',
        'type': 'integer',
        'required': True
    }],
    'responses': {
        200: {'description': 'User deleted'},
        404: {'description': 'User not found'}
    }
})
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)
