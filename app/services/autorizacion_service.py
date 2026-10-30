
# Proyecto: MuebleTech VES
# Servicio de autorización de usuarios

from functools import wraps
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db
from app.models.usuario_db import UsuarioDB


def roles_required(*roles_permitidos):
    """
    Permite el acceso únicamente a usuarios
    autenticados con uno de los roles autorizados.
    """

    def decorador(func):

        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs):

            id_usuario = get_jwt_identity()

            try:
                id_usuario = int(id_usuario)
            except (TypeError, ValueError):
                return jsonify({
                    "error": "Identidad de usuario inválida"
                }), 401

            usuario = db.session.get(UsuarioDB, id_usuario)

            if usuario is None or not usuario.activo:
                return jsonify({
                    "error": "Usuario no autorizado"
                }), 403

            # Compatible con roles anteriores y nuevos
            rol = str(usuario.rol).upper()

            if rol == "USUARIO":
                rol = "CONSULTA"

            if rol not in roles_permitidos:
                return jsonify({
                    "error": "No tiene permisos para esta operación"
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorador


def admin_required(func):
    """Solo ADMIN puede realizar esta operación."""
    return roles_required("ADMIN")(func)


def editor_required(func):
    """EDITOR y ADMIN pueden crear o editar."""
    return roles_required("EDITOR", "ADMIN")(func)
