FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install --upgrade pip && pip install "uvicorn[standard]" fastapi "python-jose[cryptography]" passlib[bcrypt] asyncpg sqlalchemy[asyncio] psycopg[binary]
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
