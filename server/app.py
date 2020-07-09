import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

from pprint import pprint as pp

from donnees import session
from historiqueManager import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# TEST DE MODIFICATION DES DONNEES ET RECUPERATION
# session.get('investigateurs').get('1').get('competences')["vitesse"] = session.get('investigateurs').get('1').get('competences')["vitesse"] + 1
# pp(session.get('investigateurs').get('1').get('competences'))
# pp('ajouter lolo')
# pp(AjouterEtape('lolo'))
# pp('ajouter toto')
# pp(AjouterEtape('toto'))
# pp(pp(session.get('historique').get('etapes')))

@app.route('/check/<nomEtape>', methods=['GET'])
def check(nomEtape):
    return jsonify(VerifierHistorique(nomEtape))

@app.route('/test1', methods=['GET'])
def test1():
    return jsonify(session)

@app.route('/test2', methods=['GET'])
def test2():
    session['monstre'] = 'Chthonien'
    return jsonify(session)

# EXEMPLES D'UTILISATION

# @app.route('/books', methods=['GET', 'POST'])
# def all_books():
#     response_object = {'status': 'success'}
#     if request.method == 'POST':
#         post_data = request.get_json()
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book added!'
#     else:
#         response_object['books'] = BOOKS
#     return jsonify(response_object)

# @app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
# def single_book(book_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book updated!'
#     if request.method == 'DELETE':
#         remove_book(book_id)
#         response_object['message'] = 'Book removed!'
#     return jsonify(response_object)


if __name__ == '__main__':
    app.run()


# def remove_book(book_id):
#     for book in BOOKS:
#         if book['id'] == book_id:
#             BOOKS.remove(book)
#             return True
#     return False

# BOOKS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]