from celery import Celery
import os

celery = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_BACKEND_URL", "redis://redis:6379/1")
)

@celery.task
def long_running(n):
    import time
    time.sleep(n)
    return f"done {n}"
