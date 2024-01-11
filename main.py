# Connexion à la base de donnée

import mysql.connector

# # Paramètres de connexion à la base de données

config = {
    "user": "root",
    "password": "",
    "host": "localhost",  # 127.0.0.1
    "database": "bibliotheque_musicale",
}

# Établir la connexion à la base de données

mydb = mysql.connector.connect(**config)


# # Init d'un curseur
# mycursor = mydb.cursor(dictionary=True)

# mycursor.execute("SELECT * FROM villes_france_free")

# liste_villes = mycursor.fetchall()

# for ville in liste_villes:
#     print(ville["ville_nom"])


# Afficher le menu


# 1. Afficher les titres
mycursor = mydb.cursor()

sql = "SELECT titre_music, nom_chanteur FROM chanteur INNER JOIN music ON chanteur.id_chanteur = music.id_music ORDER BY titre_music, nom_chanteur "

mycursor.execute(sql)

titre_music = mycursor.fetchall()
nom_chanteur = mycursor.fetchall()

for x in titre_music:
    print(x)

for x in nom_chanteur:
    print(x)


# 2. Ajouter un titre
