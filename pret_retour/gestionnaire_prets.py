# Dans pret_retour/gestionnaire_prets.py
from .pret_retour import PretRetour
from datetime import datetime

class GestionnairePrets:
    def __init__(self):
        self.prets = []

    def enregistrer_pret(self, livre, utilisateur):
        nouveau_pret = PretRetour(livre, utilisateur, datetime.now())
        self.prets.append(nouveau_pret)

    def lister_prets(self):
        return [str(pret) for pret in self.prets]

    def charger_prets_depuis_db(self, db_manager):
        # À adapter en fonction de la structure de la base de données
        # Utilise db_manager pour charger les prêts depuis la base de données
        pass
