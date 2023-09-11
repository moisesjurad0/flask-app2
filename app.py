from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restplus import Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

app.config.from_object('app.config')

# Swagger Configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# MongoDB Configuration
db = MongoEngine(app)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)
