
from datetime import datetime, timezone
from app.extensions import db


class UsuarioDB(db.Model):

    __tablename__ = "usuarios"

    # Identificador del usuario
    id_usuario = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Nombre del usuario
    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    # Correo electrónico único
    correo = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    # Contraseña protegida mediante bcrypt
    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    # Roles permitidos: CONSULTA, EDITOR y ADMIN
    rol = db.Column(
        db.String(20),
        nullable=False,
        default="CONSULTA"
    )

    # Estado de la cuenta
    activo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # Fecha de registro
    fecha_registro = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )
