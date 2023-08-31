from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
# The `Zookeeper` model should contain a `name`, a `birthday`, and a list of
#   `animals` that they take care of.
class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    birthday = db.Column(db.String())
    animals = db.relationship('Animal', backref="zookeeper")

    def __repr__(self):
       return f'<{self.__class__.__name__}: {self.name}, {self.birthday}>' 

   
# - The `Enclosure` model should contain an `environment` (grass, sand, or water),
#   an `open_to_visitors` boolean, and a list of `animals`.
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure')

    def __repr__(self):
       return f'<{self.__class__.__name__}: {self.environment}, {self.open_to_visitors}>'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    species = db.Column(db.String(80))
    zookepper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"))
    enclosures_id = db.Column(db.Integer, db.ForeignKey("enclosures.id"))

    def __repr__(self):
       return f'<{self.__class__.__name__}: {self.name}, {self.species}, {self.zookeeper}, {self.enclosure}>'