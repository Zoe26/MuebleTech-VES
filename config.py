
# Configuración de PostgreSQL - MuebleTech VES

import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

# Cargar las variables del archivo .env
load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
