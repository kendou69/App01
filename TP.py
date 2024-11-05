import requests
import json
import os

def fetch_data(limit=100):
    """Récupère les données JSON de l'API pour la région Auvergne-Rhône-Alpes avec tri et limite."""
    url = (
        "https://odre.opendatasoft.com/api/records/1.0/search/?dataset=eco2mix-regional-tr"
        "&refine.libelle_region=Auvergne-Rhône-Alpes"
        "&refine.date=2024-03-7"
        f"&rows={limit}"  # Limitation du nombre de résultats
        "&sort=date_heure"  # Tri par date_heure
    )
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        print("Données récupérées avec succès.")
        return response.json()  # Renvoie les données en format JSON
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la récupération des données :", e)
        return None
    except json.JSONDecodeError:
        print("Erreur de conversion JSON.")
        return None

def save_json(data, filename="data.json"):
    """Sauvegarde les données JSON dans un fichier pour vérification."""
    try:
        full_path = os.path.join(os.getcwd(), filename)
        with open(full_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Données JSON sauvegardées dans {full_path}")
    except IOError as e:
        print(f"Erreur lors de l'enregistrement des données JSON : {e}")

# Exécution des fonctions
data = fetch_data(limit=100)  # Spécifier la limite
if data:
    # Sauvegarde des données JSON dans un fichier pour inspection
    save_json(data)
else:
    print("Les données n'ont pas pu être récupérées.")
