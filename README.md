# API Résultats Baccalauréat Madagascar

Cette API permet de rechercher les résultats du baccalauréat à Madagascar en interrogeant dynamiquement les sources officielles (actuellement basée sur les données de la province d'Antsiranana).

## Installation

1. Installez les dépendances :
   ```bash
   pip install flask requests beautifulsoup4
   ```

2. Lancez l'API :
   ```bash
   python api.py
   ```

## Utilisation

### Rechercher un candidat par nom

**Route :** `GET /recherche?bacc={NOM_PRENOM}`

**Exemple :**
`http://localhost:5000/recherche?bacc=RAKOTO`

**Réponse JSON :**
```json
{
  "count": 7,
  "query": "RAKOTO",
  "results": [
    {
      "admis": "Admis",
      "centre": "ANDAPA",
      "ecole": "LP AGAPE ANDAPA",
      "mention": "PASSABLE",
      "nom_prenoms": "ANDRIANINA Rakotonantoandro Innocenti",
      "num_inscription": "2379272",
      "serie": "A2"
    },
    ...
  ],
  "source": "https://univants.mg/bacc/resultat_bacc.html",
  "timestamp": "2026-04-07 00:33:46"
}
```

## Sources analysées
- https://bacc.digital.gov.mg/ (Portail national - résultats 2026 en attente)
- https://univants.mg/bacc/resultat_bacc.html (Province d'Antsiranana - Données actives)
- https://bacc.univ-fianarantsoa.mg/ (Province de Fianarantsoa)
