# vérifie si un element nomEtape est dans la liste historique
# nomEtape: str = nom de l'étape
# return: bool = True si l'étape est dans l'historique, False sinon
def verifierHistorique(nomEtape, managerDeSession):
    hist = managerDeSession.session.get('historique').get('etapes')
    # Si nomEtape est deja en historique
    if(nomEtape in hist):
        return True
    # Si nomEtape n'est pas encore en historique
    else:
        return False

# Ajoute un element nomEtape dans la liste historique
# nomEtape: str = nom de l'étape
# return: bool = True si l'étape n'existe pas deja et a ete ajoutée dans l'historique
#                False si l'étape exite deja
def ajouterEtape(nomEtape, managerDeSession):
    hist = managerDeSession.session.get('historique').get('etapes')
    if(nomEtape not in hist):
        hist.append(nomEtape)
        return True
    else:
        return False

