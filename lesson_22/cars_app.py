from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from cars_db import cars_db
app = Flask(__name__)

# Конфігурація для JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Змініть на свій секретний ключ
jwt = JWTManager(app)

# Проста аутентифікація
users = {
    "test_user": "test_pass"
}


# Функція для автентифікації користувача
def authenticate(username, password):
    if username in users and users[username] == password:
        return username


# Функція для ідентифікації користувача за ідентифікатором
def identity(payload):
    username = payload['identity']
    return {"username": username}


# Ендпоінт для отримання токена доступу
@app.route('/auth', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Аутентифікація не пройшла!"}), 401

    username = authenticate(auth.username, auth.password)
    if not username:
        return jsonify({"message": "Неправильне ім'я користувача або пароль!"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# Ендпоінт для пошуку автомобілів
@app.route('/cars', methods=['GET'])
@jwt_required()
def get_cars():
    sort_by = request.args.get('sort_by')
    limit = request.args.get('limit')

    sorted_cars = sorted(cars_db.values(), key=lambda x: x.get(sort_by, 0) if sort_by else x['brand'])
    limited_cars = sorted_cars[:int(limit)] if limit else sorted_cars

    return jsonify(limited_cars), 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)