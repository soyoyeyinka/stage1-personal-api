from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API is running"
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "message": "healthy"
    }), 200

@app.route("/me", methods=["GET"])
def me():
    return jsonify({
        "name": "soyoye olayinka",
        "email": "soyoyeolayinka35@gmail.com",
        "github": "https://github.com/soyoyeyinka"
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
