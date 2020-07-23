from donnees import *
from pprint import pprint as pp
class SessionManager:
    """"""

    def __init__(self):
        """"""
        self.session = session

    def trouverDonneesSession(self,path:list):
        """
        Trouve une donnée de session a partir de son path
        path: list = chemin vers la propriété a trouver sous forme de liste de strings 
        return: any = donnée enregistrée en session
        """
        donnees = self.session
        for step in path:
            donnees = donnees.get(step)
        return donnees

    def modifierDonneesSession(self,path:list,value:any,append:bool=False):
        """
        Modifie les donnes de session
        path: list = chemin vers la propriété a modifier sous forme de liste de strings
        value: any = la valeur a enregistrer
        append: bool = si True on ajoute la valeur dans un tableau plutot que d'écraser l'ancienne valeur, False par défaut
        return: bool = True si modification
        """
        donnees = self.session
        for step in path[:-1]:
            donnees = donnees[step]
        if append == False:
            donnees[path[-1]] = value
        else:
            donnees[path[-1]].append(value)
        return True


    
