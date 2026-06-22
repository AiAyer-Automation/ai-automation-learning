from flask import Flask, jsonify, request
from tools import uppercase , lowercase , count_words , reverse_text
from storage import load_tasks, save_tasks

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

@app.route("/api/tool", methods=["POST"])
def tool():
    data = request.json
    action = data.get("action")

    if action == "upper":
        text = data.get("text", "")
        result = text.upper()
    elif action == "Lower":
        text = data.get("text", "")
        result = text.lower()
    elif action == "length":
        result = len(data.get("text", ""))
    else:
        result = "Unknown action"

    return jsonify({"result": result})

@app.route("/text", methods=["POST"])
def text_tool():
    data = request.json
    action = data.get("action")
    text = data.get("text", "")

    if action == "upper":
        result = uppercase(text)
    elif action == "lower":
        result = lowercase(text)
    elif action == "count":
        result = count_words(text)
    elif action == "reverse":
        result = reverse_text(text)
    else:
        result = "Unknown action"

    return jsonify({"result": result})

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks = load_tasks()
    tasks.append({"task": data.get("task", "No task provided")})
    
    save_tasks(tasks)
    return jsonify({"message": "Task added successfully"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)