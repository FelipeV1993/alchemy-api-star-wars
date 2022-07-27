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
class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(db.Integer, primary_key=True)
    user_name = Column(db.String(100), nullable=False, unique=True)
    password = Column(db.String(100), nullable=False,)
    email = Column(db.String(100), nullable=False, unique=True)
    name = Column(db.String(100), )
    last_name = Column(db.String(100), )

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "password": self.password,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
        }


# id init pk
# usser_name string unique
# password string
# email string
# name string NULL 
# last_name string NULL 

class People(db.Model):
    __tablename__ = 'People'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(db.Integer, primary_key=True)
    Name = Column(db.String(100), nullable=False, unique=True)
    height = Column(db.Integer, nullable=False,)
    mass = Column(db.Integer, nullable=False,)
    hair_color = Column(db.String(100), )
    skin_color = Column(db.String(100), )
    eye_color = Column(db.String(100), )
    birth_year = Column(db.String(100), )
    gender = Column(db.String(100), )

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,

        }


# People
# -
# People_id PK int
# Name varchar(200) UNIQUE 
# height int
# mass int
# hair_color string NULL 
# skin_color string
# eye_color string
# birth_year string
# gender string NULL 

class Planets(db.Model):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(db.Integer, primary_key=True)
    Name = Column(db.String(100), nullable=False, unique=True)
    rotation_period = Column(db.Integer, nullable=False,)
    orbital_period = Column(db.Integer, nullable=False,)
    diameter = Column(db.Integer, nullable=False,)
    climate = Column(db.String(100), )
    gravity = Column(db.String(100), )
    terrain = Column(db.String(100), )
    surface_water = Column(db.Integer, nullable=False,)

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }

# Planets
# -
# Planet_id PK int
# Name varchar(200) UNIQUE
# rotation_period int
# orbital_period int
# diameter int
# climate string
# gravity string
# terrain string
# surface_water init

class Vehicles(db.Model):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(db.Integer, primary_key=True)
    Name = Column(db.String(100), nullable=False, unique=True)
    model = Column(db.String(100), )
    manufacturer = Column(db.String(100), )
    cost_in_credits = Column(db.Integer, nullable=False,)
    length = Column(db.Integer, nullable=False,)
    max_atmosphering_speed = Column(db.Integer, nullable=False,)
    crew = Column(db.Integer, nullable=False,)
    passengers = Column(db.Integer, nullable=False,)

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
        }

# Vehicles
# -
# Vehicles_id PK int FK 
# Name varchar(200) UNIQUE
# model string
# manufacturer string
# cost_in_credits int
# length init
# max_atmosphering_speed init
# crew init
# passengers init



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(db.Integer, primary_key=True)
#     name = Column(db.String(100), nullable=False)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(db.Integer, primary_key=True)
#     street_name = Column(db.String(100))
#     street_number = Column(db.String(100))
#     post_code = Column(db.String(100), nullable=False)
#     person_id = Column(db.Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class Favorites(db.Model):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.

    user_id = Column(db.Integer, ForeignKey('User.id'), primary_key=True)
    planets_id = Column(db.Integer, ForeignKey('Planets.id'))
    vehicles_id = Column(db.Integer, ForeignKey('Vehicles.id'))
    people_id = Column(db.Integer, ForeignKey('People.id'))

    def serialize(self):
        return {
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "vehicles_id": self.vehicles_id,
            "people_id": self.people_id,
        }

# user_id FK >- User.id pk init
# planets_id FK >- Planets.Planet_id pk init
# vehicles_id FK >- Vehicles.Vehicles_id pk init
# people_id FK >- People.People_id pk init

## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')