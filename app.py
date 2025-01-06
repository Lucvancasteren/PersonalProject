from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Voorbeeld database (in een echt project zou je een echte database gebruiken)
cars_db = [
    {
        "id": 1,
        "brand": "BMW",
        "model": "X3",
        "year": 2018,
        "price": 29999,
        "image": "https://voorbeeld-url.com/bmw-x3.jpg"
    },
    # Voeg meer auto's toe
]

@app.route('/cars', methods=['POST'])
def get_cars():
    filters = request.json
    filtered_cars = cars_db

    if 'brand' in filters:
        filtered_cars = [car for car in filtered_cars if car['brand'].lower() == filters['brand'].lower()]
    if 'year' in filters:
        filtered_cars = [car for car in filtered_cars if car['year'] == filters['year']]
    if 'price' in filters:
        filtered_cars = [car for car in filtered_cars if car['price'] <= filters['price']]

    return jsonify(filtered_cars)

if __name__ == '__main__':
    app.run(debug=True) 