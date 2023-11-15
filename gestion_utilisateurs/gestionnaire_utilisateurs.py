# Dans gestion_utilisateurs/gestionnaire_utilisateurs.py
from .utilisateur import Utilisateur

class GestionnaireUtilisateurs:
    def _init_(self):
        self.utilisateurs = []

    def enregistrer_utilisateur(self, nom, prenom, categorie):
        nouvel_utilisateur = Utilisateur(nom, prenom, categorie)
        self.utilisateurs.append(nouvel_utilisateur)

    def lister_utilisateurs(self):
        return [str(utilisateur) for utilisateur in self.utilisateurs]

    def charger_utilisateurs_depuis_db(self, db_manager):
        # À adapter en fonction de la structure de la base de données
        # Utilise db_manager pour charger les utilisateurs depuis la base de données
        pass