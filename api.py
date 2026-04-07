from flask import Flask, request, jsonify, render_template_string
import time

app = Flask(__name__)

# Données simulées pour plusieurs provinces
DATA = {
    "Antsiranana": [
        {
            "num_inscription": "2379272",
            "nom_prenoms": "ANDRIANINA Rakotonantoandro Innocenti",
            "serie": "A2",
            "centre": "ANDAPA",
            "ecole": "LP AGAPE ANDAPA",
            "mention": "PASSABLE",
            "admis": "Admis"
        },
        {
            "num_inscription": "5182092",
            "nom_prenoms": "ATREHANTSOA Ndriana Rakotovao",
            "serie": "OSE",
            "centre": "NOSY-BE",
            "ecole": "LP ADVENTISTE NOSY-BE",
            "mention": "PASSABLE",
            "admis": "Admis"
        },
        {
            "num_inscription": "7700222",
            "nom_prenoms": "RAKOTO Asandrajato Ainay",
            "serie": "CCBTP",
            "centre": "ANTALAHA",
            "ecole": "LYCEE TECHNIQUE ANTALAHA",
            "mention": "PASSABLE",
            "admis": "Admis"
        },
        {
            "num_inscription": "4303188",
            "nom_prenoms": "RAKOTO Jean",
            "serie": "A2",
            "centre": "ANDAPA",
            "ecole": "LYCEE MIXTE ANDAPA",
            "mention": "PASSABLE",
            "admis": "Admis"
        }
    ],
    "Antananarivo": [
        {
            "num_inscription": "1029384",
            "nom_prenoms": "RAKOTOARISOA Jean Luc",
            "serie": "D",
            "centre": "ANTANANARIVO",
            "ecole": "LYCEE J.J. RABEARIVELO",
            "mention": "BIEN",
            "admis": "Admis"
        },
        {
            "num_inscription": "1029385",
            "nom_prenoms": "RANDRIANASOLO Marie",
            "serie": "A2",
            "centre": "ANTANANARIVO",
            "ecole": "LYCEE GALLIENI",
            "mention": "PASSABLE",
            "admis": "Admis"
        }
    ],
    "Fianarantsoa": [
        {
            "num_inscription": "3049586",
            "nom_prenoms": "RAKOTOMALALA Bruno",
            "serie": "C",
            "centre": "FIANARANTSOA",
            "ecole": "LYCEE RAHERIVELO RAMAMONJY",
            "mention": "TRES BIEN",
            "admis": "Admis"
        }
    ],
    "Mahajanga": [],
    "Toamasina": [],
    "Toliara": []
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Résultats BACC Madagascar</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f4f7f6; }
        .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        h2 { color: #2980b9; margin-top: 30px; }
        code { background: #f8f8f8; padding: 2px 5px; border-radius: 3px; font-family: monospace; color: #e74c3c; }
        .endpoint { background: #2c3e50; color: white; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .endpoint code { color: #f1c40f; background: transparent; }
        .example { background: #ecf0f1; border-left: 5px solid #3498db; padding: 15px; margin: 15px 0; }
        a { color: #3498db; text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; }
        .footer { margin-top: 50px; font-size: 0.9em; color: #7f8c8d; text-align: center; }
        .tag { display: inline-block; background: #3498db; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; margin-right: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 API Résultats BACC Madagascar</h1>
        <p>Bienvenue sur l'interface de documentation de l'API des résultats du Baccalauréat à Madagascar.</p>
        
        <h2>🚀 Utilisation de l'API</h2>
        <p>L'API permet de rechercher des candidats par nom et par province.</p>
        
        <div class="endpoint">
            <code>GET /recherche?bacc={NOM}&province={PROVINCE}</code>
        </div>

        <h3>Paramètres :</h3>
        <ul>
            <li><code>bacc</code> (obligatoire) : Le nom ou une partie du nom du candidat.</li>
            <li><code>province</code> (optionnel) : La province de l'examen (ex: Antsiranana, Antananarivo, Fianarantsoa).</li>
        </ul>

        <h2>🔗 Exemples de liens cliquables</h2>
        <div class="example">
            <p><strong>Recherche simple (RAKOTO) :</strong><br>
            <a href="/recherche?bacc=RAKOTO" target="_blank">/recherche?bacc=RAKOTO</a></p>
        </div>

        <div class="example">
            <p><strong>Recherche par province (RAKOTO à Antsiranana) :</strong><br>
            <a href="/recherche?bacc=RAKOTO&province=Antsiranana" target="_blank">/recherche?bacc=RAKOTO&province=Antsiranana</a></p>
        </div>

        <div class="example">
            <p><strong>Recherche spécifique (Bruno à Fianarantsoa) :</strong><br>
            <a href="/recherche?bacc=Bruno&province=Fianarantsoa" target="_blank">/recherche?bacc=Bruno&province=Fianarantsoa</a></p>
        </div>

        <h2>📍 Provinces supportées</h2>
        <p>
            <span class="tag">Antananarivo</span>
            <span class="tag">Antsiranana</span>
            <span class="tag">Fianarantsoa</span>
            <span class="tag">Mahajanga</span>
            <span class="tag">Toamasina</span>
            <span class="tag">Toliara</span>
        </p>
    </div>
    <div class="footer">
        Développé pour la consultation rapide des résultats BACC Madagascar.
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/recherche', methods=['GET'])
def recherche():
    bacc_query = request.args.get('bacc', '')
    province_query = request.args.get('province', '')
    
    if not bacc_query:
        return jsonify({"error": "Veuillez fournir un nom via le paramètre ?bacc="}), 400
    
    results = []
    
    # Si une province est spécifiée
    if province_query:
        if province_query in DATA:
            province_data = DATA[province_query]
            results = [r for r in province_data if bacc_query.lower() in r['nom_prenoms'].lower()]
        else:
            return jsonify({"error": f"Province '{province_query}' non reconnue. Provinces valides: {', '.join(DATA.keys())}"}), 404
    else:
        # Recherche dans toutes les provinces
        for province, candidates in DATA.items():
            for c in candidates:
                if bacc_query.lower() in c['nom_prenoms'].lower():
                    # On ajoute la province à l'objet résultat pour plus de clarté
                    res_with_prov = c.copy()
                    res_with_prov['province'] = province
                    results.append(res_with_prov)
    
    return jsonify({
        "query": bacc_query,
        "province_filter": province_query if province_query else "Toutes",
        "count": len(results),
        "results": results,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
