from flask import Flask, request, jsonify, render_template_string
import time
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Données simulées pour les autres provinces (en attendant d'avoir leurs API réelles)
STATIC_DATA = {
    "Antananarivo": [
        {
            "num_inscription": "1029384",
            "nom_prenoms": "RAKOTOARISOA Jean Luc",
            "serie": "D",
            "centre": "ANTANANARIVO",
            "ecole": "LYCEE J.J. RABEARIVELO",
            "mention": "BIEN",
            "admis": "Admis"
        }
    ],
    "Mahajanga": [],
    "Toamasina": [],
    "Toliara": []
}

def search_antsiranana_real(query):
    """Effectue une recherche réelle sur l'API d'Antsiranana"""
    url = "https://univants.mg/bacc/api/search.php"
    params = {
        "action": "search",
        "nom_prenom": query
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and "data" in data:
                return [
                    {
                        "num_inscription": item.get("numero_candidat"),
                        "nom_prenoms": item.get("nom_prenom"),
                        "serie": item.get("option"),
                        "centre": item.get("centre"),
                        "ecole": item.get("etablissement"),
                        "mention": item.get("mention"),
                        "admis": "Admis" if item.get("mention") else "Inconnu",
                        "province": "Antsiranana"
                    }
                    for item in data["data"]
                ]
    except Exception as e:
        print(f"Erreur Antsiranana: {e}")
    return []

def search_fianarantsoa_real(query):
    """Effectue une recherche réelle sur le site de Fianarantsoa"""
    url = "https://bacc.univ-fianarantsoa.mg/"
    try:
        # Tentative de recherche par POST
        response = requests.post(url, data={"nom_candidat": query, "btn_nom": "Rechercher"}, timeout=10)
        print(f"Fianarantsoa POST status: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            # Chercher le tableau de résultats
            table = soup.find('table')
            if table:
                rows = table.find_all('tr')[1:] # Ignorer l'en-tête
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 5:
                        results.append({
                            "num_inscription": cols[0].text.strip(),
                            "nom_prenoms": cols[1].text.strip(),
                            "serie": cols[2].text.strip(),
                            "centre": cols[3].text.strip(),
                            "mention": cols[4].text.strip(),
                            "admis": "Admis" if "Non Admis" not in cols[4].text else "Non Admis",
                            "province": "Fianarantsoa"
                        })
            print(f"Fianarantsoa results found: {len(results)}")
            return results
    except Exception as e:
        print(f"Erreur Fianarantsoa: {e}")
    return []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Résultats BACC Madagascar (LIVE)</title>
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
        .live-badge { background: #27ae60; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.7em; vertical-align: middle; margin-left: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 API Résultats BACC Madagascar <span class="live-badge">LIVE</span></h1>
        <p>Cette API interroge en temps réel les serveurs officiels pour plusieurs provinces.</p>
        
        <h2>🚀 Utilisation de l'API</h2>
        <div class="endpoint">
            <code>GET /recherche?bacc={NOM}&province={PROVINCE}</code>
        </div>

        <h2>🔗 Exemples de liens cliquables (Temps Réel)</h2>
        <div class="example">
            <p><strong>Recherche "Fanantenana" à Antsiranana :</strong><br>
            <a href="/recherche?bacc=Fanantenana&province=Antsiranana" target="_blank">/recherche?bacc=Fanantenana&province=Antsiranana</a></p>
        </div>

        <div class="example">
            <p><strong>Recherche "RAKOTO" à Fianarantsoa :</strong><br>
            <a href="/recherche?bacc=RAKOTO&province=Fianarantsoa" target="_blank">/recherche?bacc=RAKOTO&province=Fianarantsoa</a></p>
        </div>

        <h2>📍 Provinces supportées</h2>
        <p>
            <span class="tag">Antsiranana (LIVE)</span>
            <span class="tag">Fianarantsoa (LIVE)</span>
            <span class="tag">Antananarivo (Démo)</span>
            <span class="tag">Mahajanga (Bientôt)</span>
            <span class="tag">Toamasina (Bientôt)</span>
            <span class="tag">Toliara (Bientôt)</span>
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
    
    # Logique de recherche par province
    if province_query == "Antsiranana":
        results = search_antsiranana_real(bacc_query)
    elif province_query == "Fianarantsoa":
        results = search_fianarantsoa_real(bacc_query)
    elif province_query in STATIC_DATA:
        results = [r for r in STATIC_DATA[province_query] if bacc_query.lower() in r['nom_prenoms'].lower()]
        for r in results: r['province'] = province_query
    elif not province_query:
        # Recherche globale
        results.extend(search_antsiranana_real(bacc_query))
        results.extend(search_fianarantsoa_real(bacc_query))
        for prov, candidates in STATIC_DATA.items():
            for c in candidates:
                if bacc_query.lower() in c['nom_prenoms'].lower():
                    res_with_prov = c.copy()
                    res_with_prov['province'] = prov
                    results.append(res_with_prov)
    else:
        return jsonify({"error": f"Province '{province_query}' non reconnue."}), 404
    
    return jsonify({
        "query": bacc_query,
        "province_filter": province_query if province_query else "Toutes",
        "count": len(results),
        "results": results,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
