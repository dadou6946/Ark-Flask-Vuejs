session = {
    'partie': {
        'nombreJoueurs':2,
    },
    'historique': {
        'dernier': '', # mix-ally-package
        'etapes': [], # 'choose-characters', 'choose-players', 'mix-ally-package'
    },
    'investigateurs':{
        # Exemple d'investigqteur avec des donnees
        # '1': {
        #     'nom': 'Joe Diamonds',
        #     'joueur':'sylvain',
        #     'statut': 'ok',
        #     'lieu': {
        #         'actuel': {
        #             'nom': 'Administration',
        #             'id': 17
        #         },
        #         'maison': {
        #             'nom': 'Poste de police',
        #             'id': 9
        #         }
        #     },
        #     'resistance': {
        #         'actuelle':7,
        #         'max':7
        #     },
        #     'santeMentale': {
        #         'actuelle':3,
        #         'max':3
        #     },
        #     'competences': {        
        #         'vitesse': 1,
        #         'discretion': 3,
        #         'vigueur': 4,
        #         'volonté': 2,
        #         'savoir': 1,
        #         'chance': 3,
        #     },
        #     'possessions':[
        #         {
        #             'id': 2,
        #             'nom': "hache",
        #             'propriétaire': 1,
        #             'paquet': "commun",
        #             'status': True, #utilisable si true, false si objet déchargé
        #             'cost': 5,
        #             'image': "hache.jpg",
        #             'type': 'arme', #(utilisable, arme, sort, tome, consommable),
        #             'hand': 1,
        #             'texte': "Arme physique<br>+4 aux tests de Combat",
        #             'modificateur':
        #             {
        #                 'typeDegat': "magique",
        #                 'aptitude': "combat",
        #                 'valeur': +1,
        #                 'valeurAlternative': +4,
        #                 'conditionAlternative': "1 main libre",
        #             },
        #             'action':
        #             {
        #                 'nom': "decharger", # destroy
        #                 'quand': "mouvement",
        #                 'gainValeur ': 2,
        #                 'gainType': "mouvement",
        #             },
        #             'passif':
        #             {
        #                 'valeurPassif': +1,
        #                 'aptitudePassif': "test d'horreur",
        #             }
        #         }
        #     ]
        # },
    },
    'monstres': [
        # Exemple de montre
        # {
        #     'nom': 'Vampire',
        #     'conscience': -3,
        #     'mouvement': 'normal',
        #     'symbole': 'lune',
        #     'capacites': [
        #         'mort-vivant',
        #         'résistance physique'
        #     ],
        #     'texteAmbiance': 'C\était une bête dans la tombe. Il tendait ses mains vers nous et retroussait ses lèvres, atiré par le sang dans nos veines.',
        #     'horreur': {
        #         'valeur': +0,
        #         'degat': 2
        #     },
        #     'force': 2,
        #     'combat': {
        #         'valeur': -3, 
        #         'degat': 3
        #     }
        # }
    ],
    'ancien': {
        # Exemple d'ancien
        # 'nom': 'Yig',
        # 'valeurCombat': -3,
        # 'capaciteDefensive': 'aucun',
        # 'adorateurs': {
        #     'texte': 'Les adorateurs de Yig sont en réalité des membres du Peuple Serpent déguisés. Leur morsure est très venimeuse. Les Cultistes ont une valeur de combat de +0 et des dégâts de combat de 4 résistances.',
        #     'passif': 
        #     {
        #         'cible': 'cultiste',
        #         'effets': [
        #         {
        #             'cle':'combat',
        #             'valeur': +0,
        #         },
        #         {   
        #             'cle': 'degats',
        #             'valeur': 4
        #         }
        #         ] 
        #     }
        # },
        # 'pouvoirs':[
        #     {
        #         'titre': 'La colère de Yig',
        #         'texte': 'Tant que Yig est plongé dans son sommeil, il gagne un pion destin quand un cultiste est battu ou quand un investigateur est perdu dans le temps et l\'espace.'
        #     },
        #     {
        #         'titre': 'Début de bataille',
        #         'texte': 'Chaque investigateur est Maudit. Un investigateur qui est déjà Maudit est dévoré.'
        #     }
        # ],
        # 'attaque': {
        #     'texte': 'Chaque investigateur doit réussir un test de Vitesse (+1) ou perdre 1 Santé Mentale et 1 Résistance. Le modificateur de test diminue de 1 à chaque tour (+0 au deuxième tour, -1 au troisième, etc.)'
        # },
        # 'echelleDestin': {
        #     'actuelle': 0,
        #     'max': 10
        # }
    },
    'objetsDisponibles': {
        'allies': [], # avoir une liste MELANGEE de 11 id d'allies => 1,2,3,4,5,6,7,8,9,10,11
        'communs':[], # avoir une liste MELANGEE de x id de cartes communes, uniques, ...
        'uniques':[],
        'competences':[],
        'sorts':[],
        'speciaux':[],
    },
    'sites': [
        { 'name': 'Boutique<br>de<br>souvenir', 'id': '1', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'orange', 'portal': [], 'marker': [], 'white': 27, 'black': 27, },
        { 'name': 'Journal', 'id': '2', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'orange', 'portal': [], 'marker': [], 'white': 27, 'black': 27, },
        { 'name': 'Gare', 'id': '3', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'orange', 'portal': [], 'marker': [], 'white': 27, 'black': 27, },
        { 'name': "Banque<br>d'Arkham", 'id': '4', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'white', 'portal': [], 'marker': [], 'white': 28, 'black': 28, },
        { 'name': "Asile<br>d'Arkham", 'id': '5', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'white', 'portal': [], 'marker': [], 'white': 28, 'black': 28, },
        { 'name': "Square de<br>l'indépen-<br>-dance", 'id': '6', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'white', 'portal': [], 'marker': [], 'white': 28, 'black': 28, },
        { 'name': 'Relais<br>routier<br>de Hibb', 'id': '7', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'grey', 'portal': [], 'marker': [], 'white': 29, 'black': 29, },
        { 'name': 'Restaurant<br>de Velma', 'id': '8', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'grey', 'portal': [], 'marker': [], 'white': 29, 'black': 29, },
        { 'name': 'Poste<br>de<br>-police', 'id': '9', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'grey', 'portal': [], 'marker': [], 'white': 29, 'black': 29, },
        { 'name': "L'ile<br>inexplorée", 'id': '10', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'green', 'portal': [], 'marker': [], 'white': 30, 'black': 30, },
        { 'name': 'Les<br>quais', 'id': '11', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'green', 'portal': [], 'marker': [], 'white': 30, 'black': 30, },
        { 'name': "l'Inno-<br>-mable", 'id': '12', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'green', 'portal': [], 'marker': [], 'white': 30, 'black': 30, },
        { 'name': 'Le<br>cimetière', 'id': '13', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'purple', 'portal': [], 'marker': [], 'white': 31, 'black': 31, },
        { 'name': 'La Caverne<br>noire', 'id': '14', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'purple', 'portal': [], 'marker': [], 'white': 31, 'black': 31, },
        { 'name': 'Le<br>magasin', 'id': '15', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'purple', 'portal': [], 'marker': [], 'white': 31, 'black': 31, },
        { 'name': 'Département<br>Scientifique', 'id': '16', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'yellow', 'portal': [], 'marker': [], 'white': 32, 'black': 32, },
        { 'name': 'Adminis-<br>-tration', 'id': '17', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'yellow', 'portal': [], 'marker': [], 'white': 32, 'black': 32, },
        { 'name': 'Biblio-<br>-thèque', 'id': '18', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'yellow', 'portal': [], 'marker': [], 'white': 32, 'black': 32, },
        { 'name': 'Maison<br>de la<br>sorcière', 'id': '19', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'blue', 'portal': [], 'marker': [], 'white': 33, 'black': 33, },
        { 'name': "Loge du<br>crépuscule<br>d'argent", 'id': '20', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'blue', 'portal': [], 'marker': [], 'white': 33, 'black': 33, },
        { 'name': 'Hôpital<br>Sainte<br>Marie', 'id': '21', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'red', 'portal': [], 'marker': [], 'white': 34, 'black': 34, },
        { 'name': 'Vieille<br>échoppe<br>de magie', 'id': '22', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'red', 'portal': [], 'marker': [], 'white': 34, 'black': 34, },
        { 'name': 'Les<br>bois', 'id': '23', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'red', 'portal': [], 'marker': [], 'white': 34, 'black': 34, },
        { 'name': 'Pension<br>de Ma', 'id': '24', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'brown', 'portal': [], 'marker': [], 'white': 35, 'black': 35, },
        { 'name': 'Société<br>des<br>historiens', 'id': '25', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 1, 'color': 'brown', 'portal': [], 'marker': [], 'white': 35, 'black': 35, },
        { 'name': 'Eglise<br>méridionale', 'id': '26', 'type': 'site', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'brown', 'portal': [], 'marker': [], 'white': 35, 'black': 35, },
        { 'name': 'Quartier<br>Nord', 'id': '27', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'orange', 'portal': [], 'marker': [], 'white': 28, 'black': 30, },
        { 'name': 'Centre<br>Ville', 'id': '28', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'white', 'portal': [], 'marker': [], 'white': 29, 'black': 27, },
        { 'name': 'Quartier<br>Est', 'id': '29', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'grey', 'portal': [], 'marker': [], 'white': 31, 'black': 28, },
        { 'name': 'Quartier<br>marchand', 'id': '30', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'green', 'portal': [], 'marker': [], 'white': 27, 'black': 32, },
        { 'name': 'Quartier<br>de la<br>rivière', 'id': '31', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'purple', 'portal': [], 'marker': [], 'white': 33, 'black': 29, },
        { 'name': 'Université<br>Miskatonik', 'id': '32', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'yellow', 'portal': [], 'marker': [], 'white': 30, 'black': 34, },
        { 'name': 'French<br>Hill', 'id': '33', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'blue', 'portal': [], 'marker': [], 'white': 35, 'black': 31, },
        { 'name': 'Quartier<br>Résidentiel', 'id': '34', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'red', 'portal': [], 'marker': [], 'white': 32, 'black': 35, },
        { 'name': 'Quartier<br>sud', 'id': '35', 'type': 'street', 'character': [], 'monster': [], 'event': [], 'clue': 0, 'color': 'brown', 'portal': [], 'marker': [], 'white': 34, 'black': 33, },
    ],
}

_investigateur_ = {
    'nom': '',
    'joueur':'',
    'statut': 'ok',
    'lieu': {
        'actuel': {
            'nom': '',
            'id': 0
        },
        'maison': {
            'nom': '',
            'id': 0
        }
    },
    'resistance': {
        'actuelle': 0,
        'max': 0
    },
    'santeMentale': {
        'actuelle': 0,
        'max': 0
    },
    'competences': {        
        'vitesse': 0,
        'discretion': 0,
        'vigueur': 0,
        'volonté': 0,
        'savoir': 0,
        'chance': 0,
    },
    'possessions':[],
}

_monstre_ = {
    'nom': '',
    'conscience': 0,
    'mouvement': '',
    'symbole': '',
    'capacites': [],
    'texteAmbiance': '',
    'horreur': {
        'valeur': 0,
        'degat': 0
    },
    'force': 0,
    'combat': {
        'valeur': 0, 
        'degat': 0
    }
}

_objet_ = {
    'id': 0,
    'nom': '',
    'propriétaire': 0,
    'paquet': '',
    'status': True,
    'cost': 0,
    'image': '',
    'type': '',
    'hand': 0,
    'texte': '',
    'modificateur':
    {
        'typeDegat': '',
        'aptitude': '',
        'valeur': 0,
        'valeurAlternative': 0,
        'conditionAlternative': '',
    },
    'action':
    {
        'nom': '', 
        'quand': '',
        'gainValeur ': 0,
        'gainType': '',
    },
    'passif':
    {
        'valeurPassif': 0,
        'aptitudePassif': '',
    }
}

_ancien_ = {
    'nom': '',
    'valeurCombat': 0,
    'capaciteDefensive': 'aucun',
    'adorateurs': {
        'texte': '',
        'passif': 
        {
            'cible': '',
            'effets': [
            {
                'cle':'',
                'valeur': +0,
            },
            {   
                'cle': '',
                'valeur': 0
            }
            ] 
        }
    },
    'pouvoirs':[
        {
            'titre': '',
            'texte': ''
        },
    ],
    'attaque': {
        'texte': ''
    },
    'echelleDestin': {
        'actuelle': 0,
        'max': 0
    } 
}