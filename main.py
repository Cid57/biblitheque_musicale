# Connexion à la base de donnée

import mysql.connector

# # Paramètres de connexion à la base de données

config = {
    "user": "root",
    "password": "",
    "host": "localhost",  # 127.0.0.1
    "database": "france",
}

# Établir la connexion à la base de données

mydb = mysql.connector.connect(**config)


# Init d'un curseur
mycursor = mydb.cursor(dictionary=True)

mycursor.execute("SELECT * FROM villes_france_free")

liste_villes = mycursor.fetchall()

for ville in liste_villes:
    print(ville["ville_nom"])
