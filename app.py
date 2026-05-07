from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

class DeliveryModel:
    
    def predict(self, distance, weight):
        return 0.5 + (distance * 0.2) + (weight * 0.1)
    
with open("delivery_model.pkl", "rb") as file:
    model = pickle.load(file)
    
@app.route("/")
def home():
    return "Flask Delivery Prediction API Is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.get_json()
    
    distance = data["distance"]
    weight = data["weight"]
    
    result = model.predict(distance, weight)
    
    return jsonify({
        "estimated_delivery_time": result
    })

if __name__ == "__main__":
    app.run(debug=True)