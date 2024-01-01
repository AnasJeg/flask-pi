import os

from flask import Flask, jsonify
import requests

app = Flask(__name__)

rest_port = int(os.environ.get('REST_PORT', 5000))
external_api_url = os.environ.get('EXTERNAL_API_URL', 'https://total.smarteez.eu/submit/?station=189069')


@app.route('/prices', methods=['GET'])
def fuel_prices():
    try:
        response = requests.get('https://total.smarteez.eu/submit/?station=189069')

        if response.status_code == 200:
            data = response.json()
            diesel_price = data['prix']['prix_diesel']
            gasoline_price = data['prix']['prix_essence']
            additive_price = data['prix']['prix_aditive']

            return jsonify({
                "Gasoil": float(diesel_price),
                "SansPlomb": float(gasoline_price),
                "Excellium": float(additive_price)
            })
        else:
            return jsonify({"error": f"Failed to retrieve data. Status code: {response.status_code}"})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

