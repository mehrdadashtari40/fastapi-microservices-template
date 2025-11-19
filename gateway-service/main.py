from fastapi import FastAPI, Request
import httpx
import os

AUTH_URL = os.getenv("AUTH_URL", "http://localhost:8001")
USERS_URL = os.getenv("USERS_URL", "http://localhost:8002")
TASKS_URL = os.getenv("TASKS_URL", "http://localhost:8003")

app = FastAPI(title="gateway")

client = httpx.AsyncClient()

@app.post("/login")
async def login(req: Request):
    body = await req.json()
    r = await client.post(f"{AUTH_URL}/token", json=body)
    return r.json()

@app.post("/users")
async def create_user(req: Request):
    body = await req.json()
    r = await client.post(f"{USERS_URL}/users", json=body)
    return r.json()

@app.post("/tasks/{s}")
async def create_task(s: int):
    r = await client.post(f"{TASKS_URL}/run-task/{s}")
    return r.json()
