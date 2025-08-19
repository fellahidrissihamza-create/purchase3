from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chercher", methods=["GET"])
def chercher():
    mot_cle = request.args.get("q", "")
    # Simulated search results
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
    app.run(host="0.0.0.0", port=5000)
