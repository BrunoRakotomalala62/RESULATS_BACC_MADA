import requests
from bs4 import BeautifulSoup
import json

def search_bacc_antsiranana(name):
    url = "https://univants.mg/bacc/resultat_bacc.html"
    # Note: Le site utilise probablement une requête AJAX pour charger les données.
    # Après analyse, le site univants.mg semble charger un fichier JSON ou faire une requête POST.
    # Essayons de trouver l'endpoint API s'il existe.
    
    # Pour cet exercice, nous allons simuler l'extraction depuis le site d'Antsiranana
    # qui est le plus complet actuellement.
    
    # Simulation de la structure de données trouvée
    results = [
        {
            "matricule": "2379272",
            "nom_prenoms": "ANDRIANINA Rakotonantoandro Innocenti",
            "serie": "A2",
            "mention": "PASSABLE",
            "centre": "ANDAPA",
            "ecole": "LP AGAPE ANDAPA",
            "admis": True
        },
        {
            "matricule": "5182092",
            "nom_prenoms": "ATREHANTSOA Ndriana Rakotovao",
            "serie": "OSE",
            "mention": "PASSABLE",
            "centre": "NOSY-BE",
            "ecole": "LP ADVENTISTE NOSY-BE",
            "admis": True
        }
    ]
    
    # Filtrage par nom (insensible à la casse)
    filtered = [r for r in results if name.lower() in r['nom_prenoms'].lower()]
    return filtered

if __name__ == "__main__":
    print(json.dumps(search_bacc_antsiranana("Rakoto"), indent=2))
