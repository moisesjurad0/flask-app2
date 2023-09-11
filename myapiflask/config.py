import os

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost/myapi_db')
SECRET_KEY = 'your_secret_key_here'
