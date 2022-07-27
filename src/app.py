from flask import Flask, jsonify, request, json
from flask_migrate import Migrate
from models import db, Todo, Contact, User, People, Planets, Vehicles, Favorites

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_dev.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/flask_db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos = list(map(lambda todo: todo.serialize(), todos))
    return jsonify(todos), 200

@app.route('/api/todos/<int:id>', methods=['GET'])
def get_todos_by_id(id):
    todo = Todo.query.get(id)
    return jsonify(todo.serialize()), 200

@app.route('/api/todos', methods=['POST'])
def create_todos():

    data = request.get_json()
    
    todo = Todo()
    todo.label = data['label']
    todo.done = data['done']

    db.session.add(todo) # INSERT INTO todos (label, done) VALUES ('My First Task', false);
    db.session.commit() # Finaliza el query

    return jsonify(todo.serialize()), 201


@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todos(id):
    
    
    todo = Todo.query.get(id)
    todo.label = request.json.get('label')
    todo.done = request.json.get('done')

    db.session.commit() # Finaliza el query

    return jsonify(todo.serialize()), 200


@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todos_by_id(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"msg": "Todo deleted"}), 200


# *********************User***********************


@app.route('/api/User', methods=['GET'])
def get_User():
    User = User.query.all()
    User = list(map(lambda User: User.serialize(), User))
    return jsonify(User), 200


@app.route('/api/User/<int:id>', methods=['GET'])
def get_User_by_id(id):
    User = User.query.get(id)
    return jsonify(User.serialize()), 200


@app.route('/api/User', methods=['POST'])
def create_User():

    data = request.get_json()
    
    User = User()
    User.user_name = data['user_name']
    User.password = data['password']
    User.email = data['email']
    User.name = data['name']
    User.last_name = data['last_name']


    db.session.add(User) # INSERT INTO todos (label, done) VALUES ('My First Task', false);
    db.session.commit() # Finaliza el query

    return jsonify(User.serialize()), 201


@app.route('/api/User/<int:id>', methods=['PUT'])
def update_User(id):
    
    
    User = User.query.get(id)
    User.user_name = request.json.get('user_name')
    User.password = request.json.get('password')
    User.email = request.json.get('email')
    User.name = request.json.get('name')
    User.last_name = request.json.get('last_name')


    db.session.commit() # Finaliza el query

    return jsonify(User.serialize()), 200


@app.route('/api/User/<int:id>', methods=['DELETE'])
def delete_User_by_id(id):
    User = User.query.get(id)
    db.session.delete(User)
    db.session.commit()
    return jsonify({"msg": "User deleted"}), 200

# *********************Planets******************

@app.route('/api/Planets', methods=['GET'])
def get_Planets():
    Planets = Planets.query.all()
    Planets = list(map(lambda Planets: Planets.serialize(), Planets))
    return jsonify(Planets), 200

# ***********************People********************

@app.route('/api/People', methods=['GET'])
def get_People():
    People = People.query.all()
    People = list(map(lambda People: People.serialize(), People))
    return jsonify(People), 200

# ***********************Vehicles********************

@app.route('/api/Vehicles', methods=['GET'])
def get_Vehicles():
    Vehicles = Vehicles.query.all()
    Vehicles = list(map(lambda Vehicles: Vehicles.serialize(), Vehicles))
    return jsonify(Vehicles), 200

# ***********************Favorites********************

@app.route('/api/Favorites', methods=['GET'])
def get_Favorites():
    Favorites = Favorites.query.all()
    Favorites = list(map(lambda Favorites: Favorites.serialize(), Favorites))
    return jsonify(Favorites), 200

@app.route('/api/User/<int:id>', methods=['GET'])
def get_Favorites_by_id(id):
    Favorites = Favorites.query.get(id)
    return jsonify(Favorites.serialize()), 200

if __name__ == '__main__':
    app.run()