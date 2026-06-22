from flask import Blueprint, jsonify, request
from services.storage import load_tasks, save_tasks

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "task": data.get("task")
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify({
        "message": "Task added successfully" , "task" : new_task
        }), 201


@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


@tasks_bp.route("/tasks/delete", methods=["POST"])
def delete_task():
    data = request.json
    task_id = data.get("id")
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Task deleted successfully"}), 200