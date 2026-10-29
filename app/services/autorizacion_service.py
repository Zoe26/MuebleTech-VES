
# Proyecto: MuebleTech VES
# Servicio de autorización de usuarios

from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db
from app.models.usuario_db import UsuarioDB


def admin_required(func):
    """
    Permite el acceso únicamente a usuarios
    autenticados que tengan el rol admin.
    """

    @wraps(func)
    @jwt_required()
    def wrapper(*args, **kwargs):

        # Obtener el ID del usuario desde el JWT
        id_usuario = get_jwt_identity()

        try:
            id_usuario = int(id_usuario)
        except (TypeError, ValueError):
            return jsonify({
                "mensaje": "Identidad de usuario inválida"
            }), 401

        # Consultar el usuario en PostgreSQL
        usuario = db.session.get(UsuarioDB, id_usuario)

        # Verificar que exista y esté activo
        if usuario is None or not usuario.activo:
            return jsonify({
                "mensaje": "Usuario no autorizado"
            }), 403

        # Verificar los permisos de administrador
        if usuario.rol != "admin":
            return jsonify({
                "mensaje": "No tiene permisos para esta operación"
            }), 403

        # Ejecutar el Controller autorizado
        return func(*args, **kwargs)

    return wrapper
