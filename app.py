from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)



@app.route("/predict", methods=["POST"])
def predict():
    # Yeni verileri alın
    data = request.get_json()

    # Tahmini yapın
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    
    prediction = model.predict(data["X"])

    return jsonify({"prediction": prediction[0]})

@app.route("/")
def baslangic_api():
    name=request.args.get("name")
    return jsonify(data=name)

@app.route("/param/<string:name>")
def baslangic_api2(name: str):
    return jsonify(data=name),404

if __name__ == "__main__":
    app.run()