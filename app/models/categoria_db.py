
# Proyecto: MuebleTech VES
# Sesión 5: Modelo de categorías en PostgreSQL

from app.extensions import db


class CategoriaDB(db.Model):

    # Nombre de la tabla en PostgreSQL
    __tablename__ = "categorias"

    # Clave primaria
    id_categoria = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Nombre de la categoría
    nombre = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    # Descripción opcional
    descripcion = db.Column(
        db.String(255),
        nullable=True
    )

    # Relación 1:N con productos
    productos = db.relationship(
        "ProductoDB",
        back_populates="categoria"
    )
