from flask import Flask, request, jsonify, render_template, redirect, url_for
from db import create_task, get_all_tasks, get_task_status
import os

app = Flask(__name__)



@app.route("/submit-backup", methods=["POST"])
def submit_backup():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    backup_name = request.form.get("backup_name")

    if not file or not backup_name:
        return jsonify({"error": "Missing file or backup name"}), 400

    # Save the file temporarily to process
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)

    # Create task with the saved file path
    task_id = create_task(file_path, backup_name)
    return jsonify({"task_id": task_id, "message": "File uploaded and backup task scheduled"})

@app.route("/status/<task_id>", methods=["GET"])
def get_status(task_id):
    status = get_task_status(task_id)
    if not status:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(status)

@app.route("/dashboard")
def dashboard():
    tasks = get_all_tasks()
    # Convert tasks to a format suitable for JSON
    tasks_data = [{
        "id": task.id,
        "file_path": task.file_path,
        "backup_name": task.backup_name,
        "status": task.status,
        "retries": task.retries,
        "created_at": task.created_at.strftime("%Y-%m-%d %H:%M:%S")
    } for task in tasks]
    return jsonify({"tasks": tasks_data})
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)