from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok"})

@app.route("/run")
def run_program():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400

    return jsonify({
        "result": f"Hello {name}"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000 , debug=True)