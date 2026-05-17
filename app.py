from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify(message="Hello, world!")

if __name__ == "__main__":
    # Menjalankan Flask di port 5000
    app.run(host="0.0.0.0", port=5000)