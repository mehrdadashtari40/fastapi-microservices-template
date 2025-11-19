from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean, select
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://pguser:pgpass@postgres/appdb")
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

app = FastAPI(title="users-service")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/users", status_code=201)
async def create_user(payload: dict):
    async with AsyncSessionLocal() as session:
        user = User(email=payload["email"], hashed_password=payload["password"])
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return {"id": user.id, "email": user.email}
