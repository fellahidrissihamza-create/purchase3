from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q', 'electricien')
    params = {
        "engine": "google",
        "q": query,
        "api_key": "3195e9fdfcda084142ea2316c4cc2f5f18c3104823a775cf51d7fa89679269d1",
        "hl": "fr",
        "gl": "fr"
    }

    response = requests.get("https://serpapi.com/search", params=params)

    if response.status_code == 200:
        results = response.json().get("organic_results", [])
        return jsonify(results)
    else:
        return jsonify({"error": response.status_code}), response.status_code
