#!bin/python
# -*- coding: utf-8 -*-
"""
author: Andrei Bastos
organization: Labic/Ufes
data: 30/01/2018
"""


from flask import Flask, jsonify, abort, request, url_for,  make_response
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

path_default = "/ford/api/v1.0/documents/"

documents = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route(path_default, methods=['GET'])
@auth.login_required
def get_documents():
    return jsonify({'documents': [make_public_document(document) for document in documents]})

@app.route(path_default+'<int:document_id>', methods=['GET'])
@auth.login_required
def get_document(document_id):
    document = [document for document in documents if document['id'] == document_id]
    if len(document) == 0:
        abort(404)
    return jsonify({'document': document[0]})

@app.route(path_default, methods=['POST'])
@auth.login_required
def create_document():
    if not request.json or not 'title' in request.json:
        abort(400)
    document = {
        'id': documents[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    documents.append(document)
    return jsonify({'document': document}), 201

@app.route(path_default+'<int:document_id>', methods=['PUT'])
@auth.login_required
def update_document(document_id):
    document = [document for document in documents if document['id'] == document_id]
    if len(document) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    document[0]['title'] = request.json.get('title', document[0]['title'])
    document[0]['description'] = request.json.get('description', document[0]['description'])
    document[0]['done'] = request.json.get('done', document[0]['done'])
    return jsonify({'document': document[0]})

@app.route(path_default+'<int:document_id>', methods=['DELETE'])
@auth.login_required
def delete_document(document_id):
    document = [document for document in documents if document['id'] == document_id]
    if len(document) == 0:
        abort(404)
    documents.remove(document[0])

def make_public_document(document):
    new_document = {}
    for field in document:
        if field == 'id':
            new_document['uri'] = url_for('get_document', document_id=document['id'], _external=True)
        else:
            new_document[field] = document[field]
    return new_document

@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



if __name__ == '__main__':
    app.run(debug=True)