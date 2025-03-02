FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt update && apt install -y \
    sqlite3 curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt



ENV SPW_PORT=9999 \
    SPW_DATABASE_FILENAME="database.db" \
    SPW_MIGRATIONS_FILENAME="migrations.json" \
    SPW_DATA_DIRECTORY="/app/data" \
    SPW_STATIC_FILES_DIRECTORY="/app/static" \
    SPW_COOKIE_SECRET="default_secret" \
    SPW_PASSWORD_SECRET="default_password_secret" \
    SPW_SESSION_TTL="3600"

EXPOSE ${SPW_PORT}

CMD rm -f /app/data/database.db && python3 main.py

