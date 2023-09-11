from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://db:27017/myDatabase"
api = Api(app)
mongo = PyMongo(app)

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


class Person(Resource):
    def get(self):
        people = mongo.db.people.find()
        output = []
        for person in people:
            output.append({
                'name': person['name'],
                'lastname': person['lastname'],
                'dni': person['dni']
            })
        return jsonify({'result': output})

    def post(self):
        name = request.json['name']
        lastname = request.json['lastname']
        dni = request.json['dni']
        mongo.db.people.insert(
            {'name': name, 'lastname': lastname, 'dni': dni})
        return jsonify({'result': 'Person added successfully'})

    def put(self):
        name = request.json['name']
        lastname = request.json['lastname']
        dni = request.json['dni']
        mongo.db.people.update_one(
            {'dni': dni}, {'$set': {'name': name, 'lastname': lastname}})
        return jsonify({'result': 'Person updated successfully'})

    def delete(self):
        dni = request.json['dni']
        mongo.db.people.delete_one({'dni': dni})
        return jsonify({'result': 'Person deleted successfully'})


api.add_resource(Person, '/person')

if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
    app.run(host="0.0.0.0", port=80, debug=True)
