# 🎓 API Résultats BACC Madagascar

Ce projet fournit une API simple et une interface web pour consulter les résultats du Baccalauréat à Madagascar.

## 🚀 Fonctionnalités

- **Interface Web** : Une page d'accueil explicative avec des exemples cliquables.
- **Recherche Dynamique** : Recherche par nom de candidat.
- **Filtrage par Province** : Possibilité de restreindre la recherche à une province spécifique.

## 🛠 Utilisation de l'API

L'endpoint principal est `/recherche`.

### Paramètres

| Paramètre | Description | Obligatoire |
|-----------|-------------|-------------|
| `bacc` | Nom ou partie du nom du candidat | Oui |
| `province` | Nom de la province (ex: Antsiranana, Antananarivo, Fianarantsoa) | Non |

### Exemples

- **Recherche globale** : `GET /recherche?bacc=RAKOTO`
- **Recherche par province** : `GET /recherche?bacc=RAKOTO&province=Antsiranana`

## 📦 Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/BrunoRakotomalala62/RESULATS_BACC_MADA.git
   cd RESULATS_BACC_MADA
   ```

2. Installer les dépendances :
   ```bash
   pip install flask
   ```

3. Lancer l'application :
   ```bash
   python api.py
   ```

L'interface sera accessible sur `http://localhost:5000`.

## 📍 Sources analysées
- https://bacc.digital.gov.mg/ (Portail national)
- https://univants.mg/bacc/resultat_bacc.html (Province d'Antsiranana)
- https://bacc.univ-fianarantsoa.mg/ (Province de Fianarantsoa)
