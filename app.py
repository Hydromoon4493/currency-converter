import json
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API_ID from environment variables (to keep it hidden)
API_ID = os.getenv("API_ID")

API_CONFIG = {
    "API_ID": API_ID,
    "API_URL": "https://openexchangerates.org/api"
}

# Custom conversion rates for fictional currencies
EXCHANGE_RATES = {
    "Bells": 0.0125,
    "GCS": 1.2,
    "Imperial Credits": 0.8,
    "Galleons": 5,
    "Dracma": 1
}

# Fictional currencies set
FICTIONAL_CURRENCIES = {"Bells", "GCS", "Imperial Credits", "Galleons", "Dracma"}

# Conversion rates for fantasy currencies in the converter:
# 1 USD = 1 USD
# 1 Bell = 0.0125 USD (Animal Crossing Bells)
# 1 Galactic Credit Standard (GCS) = 1.2 USD (Star Wars)
# 1 Imperial Credit = 0.8 GCS (Star Wars)
# 1 Galleon = 5 USD (Harry Potter)
# 1 Dracma = 1 USD (Greek Mythology/Fantasy)

app = Flask(__name__, template_folder=os.getcwd())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/currencies", methods=["GET"])
def get_currencies():
    """Fetch the available currencies from Open Exchange Rates and add custom fictional currencies."""
    url = f"{API_CONFIG['API_URL']}/currencies.json"
    response = requests.get(url)

    if response.status_code == 200:
        currencies = response.json()
        
        # Add custom fictional currencies
        currencies["Bells"] = "Animal Crossing Bells"
        currencies["GCS"] = "Galactic Credit Standard (Star Wars)"
        currencies["Imperial Credits"] = "Imperial Credits (Star Wars)"
        currencies["Galleons"] = "Galleons (Harry Potter)"
        currencies["Dracma"] = "Dracma (Greek Mythology)"
        
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

        # Check if the from_currency and to_currency are fictional or real
        if from_currency in FICTIONAL_CURRENCIES:
            # Custom handling for fictional currencies (GCS, Imperial Credits, etc.)
            from_rate = EXCHANGE_RATES.get(from_currency)
        else:
            from_rate = rates.get(from_currency)

        if to_currency in FICTIONAL_CURRENCIES:
            # Custom handling for fictional currencies (GCS, Imperial Credits, etc.)
            to_rate = EXCHANGE_RATES.get(to_currency)
        else:
            to_rate = rates.get(to_currency)

        # Check if the rates are valid and calculate the conversion
        if from_rate and to_rate:
            # Convert the amount using the rates
            converted_amount = amount * (to_rate / from_rate)  # Regular conversion from any currency
            return jsonify({"converted_amount": round(converted_amount, 2)})
        else:
            return jsonify({"error": "Invalid currency"}), 400
    else:
        return jsonify({"error": "Unable to fetch conversion rates"}), 500


if __name__ == "__main__":
    app.run(debug=True)
