from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_mongoengine import MongoEngine
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mydatabase',
    'host': 'mongodb://localhost/mydatabase'
}
api = Api(app)
db = MongoEngine(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class Person(db.Document):
    name = db.StringField(required=True)
    lastname = db.StringField(required=True)
    dni = db.StringField(required=True)

class PersonResource(Resource):
    def get(self, id):
        person = Person.objects(id=id).first()
        if person:
            return person.to_json()
        else:
            return {'error': 'Person not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('lastname', type=str, required=True)
        parser.add_argument('dni', type=str, required=True)
        args = parser.parse_args()

        person = Person(name=args['name'], lastname=args['lastname'], dni=args['dni'])
        person.save()

        return person.to_json(), 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('lastname', type=str, required=True)
        parser.add_argument('dni', type=str, required=True)
        args = parser.parse_args()

        person = Person.objects(id=id).first()
        if person:
            person.update(name=args['name'], lastname=args['lastname'], dni=args['dni'])
            return person.to_json(), 200
        else:
            return {'error': 'Person not found'}, 404

    def delete(self, id):
        person = Person.objects(id=id).first()
        if person:
            person.delete()
            return '', 204
        else:
            return {'error': 'Person not found'}, 404

api.add_resource(PersonResource, '/person/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)

