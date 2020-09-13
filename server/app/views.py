from app import app

import uuid
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pprint import pprint as pp

from sessionManager import *
from historiqueManager import *
from donnees import _investigateur_, _monstre_, _objet_, _ancien_

# configuration
DEBUG = True
app.config.from_object(__name__)
# Manager de session
sm = SessionManager()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# pp(sm.trouverDonneesSession(['historique']))
# path = ["historique","etapes"]
# test = sm.modifierDonneesSession(path, 'toto')

@app.route('/checker/<nomEtape>', methods=['POST'])
def check(nomEtape):
    verification = verifierHistorique(nomEtape, sm)

    # page du choix du nombre de joueurs et leurs nom 
    if verification == True:
        response_object = { 'deja': True }
    else:
        response_object = { 'deja': False }

    if nomEtape == 'choose-players':
        if verification == True:
            # on récupère le nombre de joueurs et les noms des joueurs si on les a deja enregistré
            response_object['nombreJoueurs'] = sm.trouverDonneesSession(['partie','nombreJoueurs'])
            investigateurs = sm.trouverDonneesSession(['investigateurs'])
            joueurs = []
            for inv in investigateurs.values():
                joueurs.append(inv.get('joueur'))
            response_object['joueurs'] = joueurs
        
    if nomEtape == 'choose-characters':        
        if verification == True:
            # On récupère les noms des investigateurs et le nombre de joueurs
            donnees = []
            investigateurs = sm.trouverDonneesSession(['investigateurs'])
            # pp(investigateurs)
            for inv in investigateurs.values():
                donnees.append(inv.get('nom'))
            response_object['investigateurs'] = donnees
        response_object['nombreJoueurs'] = sm.trouverDonneesSession(['partie','nombreJoueurs'])

    # retour de données
    return jsonify(response_object)

@app.route('/envoiDonnees/<nomEtape>', methods=['POST'])
def envoiDonnees(nomEtape):
    # Récupération des données envoyées
    data = request.get_json()
    pp(data)
    # Ajout de l'étape dans l'historique
    ajouterEtape(nomEtape, sm)

    # page du choix du nombre de joueurs et leurs nom 
    if nomEtape == 'choose-players':
        # maj nombre de joueur
        sm.modifierDonneesSession(['partie','nombreJoueurs'], data.get('nombreJoueur'))
        # creation des investigateurs avec le modèle _investigateur_
        cpt = 1
        for joueur in data.get('joueurs'):
            inv = _investigateur_.copy()
            inv['joueur'] = joueur.get('name')
            sm.modifierDonneesSession(['investigateurs', str(cpt)], inv, False)
            cpt = cpt + 1
    if nomEtape == 'choose-characters':
        for investigator in data.get('investigators'):
            sm.modifierDonneesSession(['investigateurs', str(investigator.get('player')), 'nom'], investigator.get('name'))
    response_object = { 'statut': True, 'donnees': sm.session}

    return jsonify(response_object)








# TEST DE MODIFICATION DES DONNEES ET RECUPERATION
# session.get('investigateurs').get('1').get('competences')["vitesse"] = session.get('investigateurs').get('1').get('competences')["vitesse"] + 1
# pp(session.get('investigateurs').get('1').get('competences'))
# pp('ajouter lolo')
# pp(ajouterEtape('lolo'))
# pp('ajouter toto')
# pp(ajouterEtape('toto'))
# pp(pp(session.get('historique').get('etapes')))
    
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


# DONNEES DE TEST

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