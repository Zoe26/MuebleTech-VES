
# MuebleTech VES
# Extensiones para PostgreSQL

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancias de las extensiones
db = SQLAlchemy()
migrate = Migrate()
