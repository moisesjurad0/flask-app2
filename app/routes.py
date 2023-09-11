from flask import request
from flask_restplus import Resource, fields, Namespace
from app import api, db
from app.models import Person

ns = Namespace('personas', description='Operaciones relacionadas con personas')

persona = ns.model('Persona', {
    'nombre': fields.String(required=True, description='Nombre de la persona'),
    'apellido': fields.String(required=True, description='Apellido de la persona'),
    'dni': fields.String(required=True, description='Documento Nacional de Identidad de la persona'),
})

@ns.route('/')
class PersonasResource(Resource):
    @ns.marshal_list_with(persona)
    def get(self):
        personas = Person.objects.all()
        return personas

    @ns.expect(persona)
    @ns.marshal_with(persona, code=201)
    def post(self):
        nueva_persona = Person(**api.payload)
        nueva_persona.save()
        return nueva_persona, 201

@ns.route('/<string:id>')
class PersonaResource(Resource):
    @ns.marshal_with(persona)
    def get(self, id):
        persona = Person.objects(id=id).first()
        if persona:
            return persona
        else:
            ns.abort(404, 'Persona no encontrada')

    @ns.expect(persona)
    @ns.marshal_with(persona)
    def put(self, id):
        persona = Person.objects(id=id).first()
        if persona:
            persona.update(**api.payload)
            return persona
        else:
            ns.abort(404, 'Persona no encontrada')

    @ns.marshal_with('', code=204)
    def delete(self, id):
        persona = Person.objects(id=id).first()
        if persona:
            persona.delete()
            return '', 204
        else:
            ns.abort(404, 'Persona no encontrada')
