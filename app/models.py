from app import db

class Person(db.Document):
    name = db.StringField(required=True)
    lastname = db.StringField(required=True)
    dni = db.StringField(required=True)

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'lastname': self.lastname,
            'dni': self.dni
        }
