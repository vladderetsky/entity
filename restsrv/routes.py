from threading import Lock
import json
from restsrv import app, request
from restsrv.models.entities import Entity

entity_store = {}
lock = Lock()


@app.route("/")
def index():
    return "Entity Service"


@app.route("/addEntity", methods=['POST'])
def add_entity():
    if request.headers.get('Content-Type') == "application/json":
        entity_id = json.loads(request.data)["entityID"]
        data = json.loads(request.data)["data"]

        lock.acquire()
        try:
            new_entity = Entity(entity_id, data)
            entity_store[entity_id] = new_entity
        finally:
            lock.release()

        json_ret = json.dumps({'permutations': new_entity.get_permutations()})
        return json_ret


@app.route("/sumEntity/entityID/<str_entity_id>", methods=['GET'])
def sum_entity(str_entity_id):
    entity_id = int(str_entity_id)
    if entity_id in entity_store:
        json_ret = json.dumps({'sum': entity_store[entity_id].sum()})
    else:
        json_ret = json.dumps({})
    return json_ret


@app.route("/updateEntity", methods=['POST'])
def update_entity():
    if request.headers.get('Content-Type') == "application/json":
        entity_id = json.loads(request.data)["entityID"]
        add_val = json.loads(request.data)["add"]

        lock.acquire()
        try:
            if entity_id in entity_store:
                entity_store[entity_id].add(add_val)
                json_ret = json.dumps({'results': entity_store[entity_id]
                                      .get_permutations()})
            else:
                json_ret = json.dumps({})
        finally:
            lock.release()

        return json_ret
