from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Delivery Prediction API Is Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    distance = data["distance"]
    weight = data["weight"]

    result = 0.5 + (distance * 0.2) + (weight * 0.1)

    return jsonify({
        "estimated_delivery_time": result
    })

if __name__ == "__main__":
    app.run(debug=True)