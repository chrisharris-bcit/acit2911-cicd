from flask import Blueprint, jsonify
from ..db.Dogs import all_dogs

dogs_bp = Blueprint('dogs', __name__)

@dogs_bp.get('/dogs')
def dogs():
    return jsonify(all_dogs), 200

@dogs_bp.get('/dogs/<id>')
def dog(id):
    if not id.isnumeric():
        return 'Error: ID must be numeric', 500
    id = int(id)
    if len(all_dogs) >= id:
        return all_dogs[id - 1], 200
    return {}, 204