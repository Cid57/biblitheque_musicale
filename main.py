# connexion à la base de données
import mysql.connector

# Remplacez les valeurs suivantes par les informations de votre propre base de données
host = "votre_host"
user = "votre_utilisateur"
password = "votre_mot_de_passe"
database = "votre_base_de_donnees"

# Établir la connexion à la base de données
connexion = mysql.connector.connect(
    host=host, user=user, password=password, database=database
)

# Verifier si la connexion a réussi
if connexion.is_connected():
    print("Connecté à la base de données")
else:
    print("Échec de la connexion à la base de données")

# Fermer la connexion
connexion.close()
