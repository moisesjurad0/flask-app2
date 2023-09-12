from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flasgger import Swagger
from flasgger import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/api'
mongo = PyMongo(app)
swagger = Swagger(app)


# @app.route('/people', methods=['GET'])
# def get_people():
#     """
#     summary: Obtiene la lista de people
#     ---
#     tags:
#         - people
#     responses:
#       200:
#         description: Lista de people
#         content:
#           application/json:
#             schema:
#               type: array
#               items:
#                 $ref: "#/definitions/People"
#     """
#     """
#     ---
#     summary: Crea una nueva people
#     requestBody:
#       required: true
#       content:
#         application/json:
#           schema:
#             $ref: "#/components/schemas/People"
#     responses:
#       200:
#         description: People creada exitosamente
#     """
#     people = mongo.db.people.find()
#     return people


# @app.route('/people/<id>', methods=['GET'])
# def get_people(id):
#     """
#     ---
#     summary: Obtiene una people por DNI
#     parameters:
#       - in: path
#         name: dni
#         required: true
#         schema:
#           type: string
#     responses:
#       200:
#         description: People encontrada
#         content:
#           application/json:
#             schema:
#               $ref: "#/components/schemas/People"
#       404:
#         description: People no encontrada
#     """
#     people = mongo.db.people.find_one({"_id": id})
#     return jsonify({"name": people["name"],
#                     "lastname": people["lastname"],
#                     "dni": people["dni"]})
#     # people = People.objects.get(id=id)
#     # return people




class PeopleSchema(Schema):
    name = fields.Str()
    lastname = fields.Str()
    dni = fields.Str()


@app.route('/people', methods=['POST'])
def create_people(body: PeopleSchema):
    """Create a cute furry People endpoint.
    ---
    post:
      description: Create a random pet
      parameters: 
        - in: body
          name: body
          required: True
          schema:
                $ref: '#/definitions/People'
      responses:
        201:
          description: If People is created
          content:
            application/json:
              status: string
    """
    data = request.get_json()
    errors = PeopleSchema.validate(data)
    if errors:
        return jsonify({'message': 'Validation errors', 'errors': errors}), 400

    # name = data.get('name')
    # lastname = data.get('lastname')
    # dni = data.get('dni')

    # people = PeopleSchema(name=name, lastname=lastname, dni=dni)
    # people_id = mongo.db.people.insert_one({"name": person["name"], "lastname": person["lastname"], "dni": person["dni"]}).inserted_id

    return jsonify(
        {"status": "New user created"}
    ), 201



    # name = request.json["name"]
    # lastname = request.json["lastname"]
    # dni = request.json["dni"]
    # people_id = mongo.db.people.insert_one(
    #     {"name": name, "lastname": lastname, "dni": dni}
    # ).inserted_id
    return jsonify(str(people_id))


# @app.route('/people/<id>', methods=['PUT'])
# def update_people(id):
#     """
#     ---
#     summary: Actualiza una people por DNI
#     parameters:
#       - in: path
#         name: dni
#         required: true
#         schema:
#           type: string
#     requestBody:
#       required: true
#       content:
#         application/json:
#           schema:
#             $ref: "#/components/schemas/People"
#     responses:
#       200:
#         description: People actualizada exitosamente
#       404:
#         description: People no encontrada
#     """
#     # data = request.get_json()
#     # people = People.objects.get(id=id)
#     # people.update(**data)
#     # people.save()
#     # return people
#     name = request.json["name"]
#     lastname = request.json["lastname"]
#     dni = request.json["dni"]
#     mongo.db.people.update_one(
#         {"_id": id}, {"$set": {"name": name, "lastname": lastname, "dni": dni}}
#     )
#     return jsonify({"message": "People updated successfully"})


# @app.route('/people/<id>', methods=['DELETE'])
# def delete_people(id):
#     # People.objects.get(id=id).delete()
#     # return 'People deleted'
#     mongo.db.people.delete_one({"_id": id})
#     return jsonify({"message": "People deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
