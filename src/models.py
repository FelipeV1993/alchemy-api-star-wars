from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), unique=True, nullable=False)
    done = db.Column(db.Boolean(), default=False)

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done
        }


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "phone": self.phone
        }