
# Proyecto: MuebleTech VES
# Sesión 5: Modelo de productos en PostgreSQL

from app.extensions import db


class ProductoDB(db.Model):

    # Nombre de la tabla
    __tablename__ = "productos"

    # Clave primaria
    codigo = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Datos del producto
    nombre = db.Column(
        db.String(150),
        nullable=False
    )

    precio = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    stock = db.Column(
        db.Integer,
        nullable=False
    )

    # Clave foránea hacia categorias
    id_categoria = db.Column(
        db.Integer,
        db.ForeignKey("categorias.id_categoria"),
        nullable=False
    )

    # Relación con CategoriaDB
    categoria = db.relationship(
        "CategoriaDB",
        back_populates="productos"
    )
