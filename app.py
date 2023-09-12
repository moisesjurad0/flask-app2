from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/mydatabase'  # Cambia la URI de MongoDB según tu configuración
api = Api(app)
mongo = PyMongo(app)

# Definir el modelo de datos para Persona
persona_model = api.model('Persona', {
    'nombres': fields.String(required=True, description='Nombres de la persona'),
    'apellidos': fields.String(required=True, description='Apellidos de la persona'),
    'dni': fields.String(required=True, description='DNI de la persona')
})

# Definir la colección en la base de datos
personas = mongo.db.personas

@api.route('/personas')
class PersonasResource(Resource):
    @api.marshal_with(persona_model, as_list=True)
    def get(self):
        """Obtener la lista de todas las personas"""
        personas_list = list(personas.find())
        return personas_list

    @api.expect(persona_model)
    @api.marshal_with(persona_model, code=201)
    def post(self):
        """Crear una nueva persona"""
        nueva_persona = request.json
        persona_id = personas.insert_one(nueva_persona).inserted_id
        nueva_persona['_id'] = persona_id
        return nueva_persona, 201

@api.route('/personas/<string:dni>')
class PersonaResource(Resource):
    @api.marshal_with(persona_model)
    def get(self, dni):
        """Obtener los detalles de una persona por DNI"""
        persona = personas.find_one({'dni': dni})
        if persona:
            return persona
        api.abort(404, f"No se encontró una persona con DNI {dni}")

    @api.expect(persona_model)
    @api.marshal_with(persona_model)
    def put(self, dni):
        """Actualizar los detalles de una persona por DNI"""
        persona_actualizada = request.json
        resultado = personas.update_one({'dni': dni}, {'$set': persona_actualizada})
        if resultado.modified_count == 1:
            persona = personas.find_one({'dni': dni})
            return persona
        api.abort(404, f"No se encontró una persona con DNI {dni}")

    def delete(self, dni):
        """Eliminar una persona por DNI"""
        resultado = personas.delete_one({'dni': dni})
        if resultado.deleted_count == 1:
            return '', 204
        api.abort(404, f"No se encontró una persona con DNI {dni}")

if __name__ == '__main__':
    app.run(debug=True)
