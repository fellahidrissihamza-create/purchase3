from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def accueil():
    return "Bienvenue sur l'API de recherche de sous-traitants !"

@app.route("/chercher", methods=["GET"])
def chercher():
    mot_cle = request.args.get("q", "")
    results = [
        {
            "nom": f"Résultat pour '{mot_cle}' - 1",
            "url": "https://example.com/1",
            "description": f"Description simulée pour '{mot_cle}' - 1"
        },
        {
            "nom": f"Résultat pour '{mot_cle}' - 2",
            "url": "https://example.com/2",
            "description": f"Description simulée pour '{mot_cle}' - 2"
        }
    ]
    return jsonify(results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
