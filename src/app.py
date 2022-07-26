from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Todo, Contact

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
    
    data = request.get_json()
    
    todo = Todo.query.get(id)
    todo.label = data['label']
    todo.done = data['done']

    db.session.commit() # Finaliza el query

    return jsonify(todo.serialize()), 200

@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todos_by_id(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"msg": "Todo deleted"}), 200


if __name__ == '__main__':
    app.run()