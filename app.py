from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

rest_port=5000

@app.route('/prices', methods=['GET'])
def fuel_prices():
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


if __name__ == '__main__':
    app.run(host="localhost", port=rest_port, debug=True)