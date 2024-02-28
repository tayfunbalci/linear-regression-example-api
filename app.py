from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def baslangic_api():
    name=request.args.get("name")
    return jsonify(data=name),404

@app.route("/param/<string:name>")
def baslangic_api2(name: str):
    return jsonify(data=name),404

if __name__ == "__main__":
    app.run()