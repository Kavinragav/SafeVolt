import os
import shutil
import time
from db import Session, Task

MAX_RETRIES = 3
POLL_INTERVAL = 5  # seconds

def process_task(task):
    print(f"[INFO] Processing task: {task.id}")
    try:
        # Ensure the backups directory exists
        os.makedirs("backups", exist_ok=True)
        # Simulate backup by copying file to "backups/" folder
        if not os.path.exists(task.file_path):
            raise FileNotFoundError(f"File {task.file_path} not found.")

        backup_path = os.path.join("backups", f"{task.backup_name}_{os.path.basename(task.file_path)}")
        shutil.copy(task.file_path, backup_path)

        # Update status in DB
        task.status = "COMPLETED"
        print(f"[SUCCESS] Task {task.id} completed.")

    except Exception as e:
        print(f"[ERROR] Task {task.id} failed: {str(e)}")
        task.retries += 1
        if task.retries >= MAX_RETRIES:
            task.status = "FAILED"
            print(f"[ALERT] Task {task.id} permanently failed after {MAX_RETRIES} retries.")
        else:
            print(f"[RETRY] Task {task.id} will be retried later.")

def run_worker():
    while True:
        session = Session()
        task = session.query(Task).filter_by(status="PENDING").order_by(Task.created_at).first()

        if task:
            process_task(task)
            session.commit()
        else:
            print("[INFO] No pending tasks. Waiting...")

        session.close()
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    run_worker()