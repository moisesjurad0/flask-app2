from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


configuration = swagger_client.Configuration()
configuration.host = "http://localhost:5000"

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dni = '1234' # str | 

try:
    # Eliminar una persona por DNI
    response=api_instance.get_personas_resource()
    response=api_instance.delete_persona_resource(dni)
    print("hello")
except ApiException as e:
    print("Exception when calling DefaultApi->delete_persona_resource: %s\n" % e)
