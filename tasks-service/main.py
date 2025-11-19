from fastapi import FastAPI
from celery_app import long_running

app = FastAPI(title="tasks-service")

@app.post("/run-task/{seconds}")
async def run_task(seconds: int):
    task = long_running.delay(seconds)
    return {"task_id": task.id}
