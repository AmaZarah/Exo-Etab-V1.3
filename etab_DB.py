
import sqlite3

def creer_base_de_donnees():
    # Spécifiez le nom du fichier de base de données SQLite
    conn = sqlite3.connect('etab.db')
    
    # Créez un curseur pour exécuter des requêtes SQL
    cursor = conn.cursor()
    
    # Exemple de création d'une table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eleves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            age INTEGER,
            genre TEXT
        )
    ''')
    
    # Sauvegarder (commit) les changements
    conn.commit()
    
    # Fermer la connexion
    conn.close()
    print("Base de données créée avec succès.")

# Appel de la fonction
creer_base_de_donnees()



def AjouterProfesseur(dateNaissance,ville,prenom,nom,vacant=False):
    return

def AjouterUtilisateurs(identifiant, motDePasse):
    return 