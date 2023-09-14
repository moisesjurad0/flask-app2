# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_persona_resource**](DefaultApi.md#delete_persona_resource) | **DELETE** /personas/{dni} | Eliminar una persona por DNI
[**get_persona_resource**](DefaultApi.md#get_persona_resource) | **GET** /personas/{dni} | Obtener los detalles de una persona por DNI
[**get_personas_resource**](DefaultApi.md#get_personas_resource) | **GET** /personas | Obtener la lista de todas las personas
[**post_personas_resource**](DefaultApi.md#post_personas_resource) | **POST** /personas | Crear una nueva persona
[**put_persona_resource**](DefaultApi.md#put_persona_resource) | **PUT** /personas/{dni} | Actualizar los detalles de una persona por DNI


# **delete_persona_resource**
> delete_persona_resource(dni)

Eliminar una persona por DNI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
dni = 'dni_example' # str | 

try:
    # Eliminar una persona por DNI
    api_instance.delete_persona_resource(dni)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_persona_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dni** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persona_resource**
> Persona get_persona_resource(dni, x_fields=x_fields)

Obtener los detalles de una persona por DNI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
dni = 'dni_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Obtener los detalles de una persona por DNI
    api_response = api_instance.get_persona_resource(dni, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_persona_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dni** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Persona**](Persona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_personas_resource**
> list[Persona] get_personas_resource(x_fields=x_fields)

Obtener la lista de todas las personas

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Obtener la lista de todas las personas
    api_response = api_instance.get_personas_resource(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_personas_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[Persona]**](Persona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_personas_resource**
> Persona post_personas_resource(payload, x_fields=x_fields)

Crear una nueva persona

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
payload = swagger_client.Persona() # Persona | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Crear una nueva persona
    api_response = api_instance.post_personas_resource(payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_personas_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Persona**](Persona.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Persona**](Persona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_persona_resource**
> Persona put_persona_resource(dni, payload, x_fields=x_fields)

Actualizar los detalles de una persona por DNI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
dni = 'dni_example' # str | 
payload = swagger_client.Persona() # Persona | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Actualizar los detalles de una persona por DNI
    api_response = api_instance.put_persona_resource(dni, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_persona_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dni** | **str**|  | 
 **payload** | [**Persona**](Persona.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Persona**](Persona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

