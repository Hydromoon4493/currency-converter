from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))  # Set template folder to current directory

# Replace this with your actual API key from https://www.exchangerate-api.com/
API_KEY = "your_api_key_here"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

@app.route("/")
def index():
    return render_template("index.html")  # Load frontend UI

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    base_currency = data.get("from_currency")
    target_currency = data.get("to_currency")
    amount = float(data.get("amount"))

    # Fetch exchange rates
    response = requests.get(API_URL)
    exchange_rates = response.json().get("conversion_rates", {})

    if base_currency not in exchange_rates or target_currency not in exchange_rates:
        return jsonify({"error": "Invalid currency code"}), 400

    # Calculate converted amount
    conversion_rate = exchange_rates[target_currency] / exchange_rates[base_currency]
    converted_amount = amount * conversion_rate

    return jsonify({
        "from_currency": base_currency,
        "to_currency": target_currency,
        "original_amount": amount,
        "converted_amount": round(converted_amount, 2),
        "rate": round(conversion_rate, 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
