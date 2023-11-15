# Dans base_de_donnees/db_manager.py
import sqlite3

class DatabaseManager:
    def _init_(self, db_file="bibliotheque.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def creer_tables(self):
        # À adapter en fonction des modèles de données (livres, utilisateurs, prêts)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livres (
                id INTEGER PRIMARY KEY,
                titre TEXT,
                auteur TEXT,
                genre TEXT,
                isbn TEXT
            )
        """)
        # Crée d'autres tables pour les utilisateurs, les prêts, etc.

    def sauvegarder_livre(self, livre):
        # À adapter en fonction de la structure de la base de données
        self.cursor.execute("INSERT INTO livres VALUES (?, ?, ?, ?, ?)", (livre.id, livre.titre, livre.auteur, livre.genre, livre.isbn))
        self.conn.commit()

    # Ajoute des méthodes similaires pour sauvegarder/charger les utilisateurs, prêts, etc.

# Instancie le gestionnaire de base de données
db_manager = DatabaseManager()
db_manager.creer_tables()