from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the API!"})


@app.route("/run")
def run():
    task = request.args.get("task")
    if task == "hello":
        return jsonify({"result": "Hello, World!"})
    else:
        return jsonify({"error": "Unknown task"}), 400


@app.route("/api/hello", methods=["POST"])
def api_hello():
    data = request.json
    name = data.get("name" , "unknown")

    return jsonify({"result": f"Hello, {name}"})


if __name__ == "__main__":
    app.run(debug=True)