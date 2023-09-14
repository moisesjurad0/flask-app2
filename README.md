# flask-app2

## requirements

- flask
- flask_restx
- flask_pymongo

## steps

- create your api with flask,
- add swagger tags with flask_restx
- create mongodb connection with flask_pymongo
- create docker compose
- run compose (can rebuild it with ``docker compose --build``), using flask-restx the initial page will be the swagerUI
- use the swagger.json and generate a client specific por python (import into swaggerhub and generate from there)
- download the client compressed in tar
- install the client with pip as if it was an ordinary python package
- use it. In this case I'm using it in `try_client.py`

## notes

- I've save the swagger.json file into the folder swagger, but this file was generated at initial lunch of the server
- in the same folder (swagger) i've saved the client uncompress only for referential purpouses
