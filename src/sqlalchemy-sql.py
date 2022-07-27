from models import db, Todo, Contact, User, People, Planets, Vehicles, Favorites

""" 
SQL:

INSERT INTO todos (label, done) VALUES ('My First Task', false);

"""

todo = Todo()
todo.label = "My First Task"
todo.done = False

db.session.add(todo) # INSERT INTO todos (label, done) VALUES ('My First Task', false);
db.session.commit() # Finaliza el query


""" 
SQL:

UPDATE todos SET label="My 1st Task", done=true WHERE id=1;

"""

todo = Todo.query.get(1)
todo.label = "My 1st Task"
todo.done = True

db.session.commit()