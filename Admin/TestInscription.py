import mysql.connector

def insert_user(nom, prenom, email, mot_de_passe):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="vacataire",
            port=8889 
        )
        cur = connection.cursor()

     
        query_personne = "INSERT INTO administrateur (Nom, Prenom, Email, Mot_Passe) VALUES (%s, %s, %s, %s)"
        cur.execute(query_personne, (nom, prenom, email, mot_de_passe))
        connection.commit()

        id_personne = cur.lastrowid

        connection.commit()
        connection.close()

        print("Inscription réussie")
    
    except Exception as ex:
        print(f"Problème d'inscription: {str(ex)}")


# Insérer un administrateur
insert_user('Py', 'misterpy', 'py@gmail.com', '1234')

# Insérer un enseignant
insert_user('Agoh', 'chris', 'agohchris90@gmail.com', 'py')
