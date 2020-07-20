from donnees import *
from pprint import pprint as pp
class SessionManager:
    """"""

    def __init__(self):
        """"""
        self.session = session

    def trouverDonneesSession(self,path:list):
        """"""
        donnees = self.session
        for step in path:
            donnees = donnees.get(step)
        return donnees

    def modifierDonneesSession(self,path:list,value:any):
        """"""
        donnees = self.session
        for step in path[:-1]:
            donnees = donnees[step]
        donnees[path[-1]] = value
        return True


    
