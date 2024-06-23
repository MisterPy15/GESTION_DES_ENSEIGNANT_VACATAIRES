import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="vacataire",
            port=8889  # Assurez-vous que le port est correct
        )
        if connection.is_connected():
            print("Connexion réussie à la base de données")
        return connection
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        return None
