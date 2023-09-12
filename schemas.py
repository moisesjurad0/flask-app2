from flasgger import Schema, fields

class PeopleSchema(Schema):
    name = fields.Str()
    lastname = fields.Str()
    dni = fields.Str()
