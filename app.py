import json
from flask import Flask, render_template, request, jsonify
import requests
import os

# Store your API_ID in a configuration variable
API_CONFIG = {
    "API_ID": "4a9509426cc64f2884122be3e6802bf4",
    "API_URL": "https://openexchangerates.org/api"
}

app = Flask(__name__, template_folder=os.getcwd())  # Explicitly set the template folder to the current directory

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/currencies", methods=["GET"])
def get_currencies():
    # Fetch the available currencies from Open Exchange Rates
    url = f"{API_CONFIG['API_URL']}/currencies.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        currencies = response.json()
        return jsonify(currencies)
    else:
        return jsonify({"error": "Unable to fetch currencies"}), 500

@app.route("/convert", methods=["POST"])
def convert_currency():
    data = request.get_json()
    amount = float(data.get("amount"))
    from_currency = data.get("from_currency")
    to_currency = data.get("to_currency")

    # Fetch the conversion rates from Open Exchange Rates
    url = f"{API_CONFIG['API_URL']}/latest.json?app_id={API_CONFIG['API_ID']}"
    response = requests.get(url)

    if response.status_code == 200:
        rates = response.json()["rates"]
        
        if from_currency == "USD":
            from_rate = 1
        else:
            from_rate = rates.get(from_currency)
        
        if to_currency == "USD":
            to_rate = 1
        else:
            to_rate = rates.get(to_currency)

        if from_rate and to_rate:
            converted_amount = amount * (to_rate / from_rate)
            return jsonify({"converted_amount": round(converted_amount, 2)})
        else:
            return jsonify({"error": "Invalid currency"}), 400
    else:
        return jsonify({"error": "Unable to fetch conversion rates"}), 500

if __name__ == "__main__":
    app.run(debug=True)
