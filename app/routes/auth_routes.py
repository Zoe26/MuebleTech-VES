
# Proyecto: MuebleTech VES
# Rutas de autenticación

from flask import Blueprint
from app.extensions import limiter

from app.controllers.auth_controller import (
    registrar_usuario,
    iniciar_sesion
)


auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/api/auth"
)


# Registro exigido por el profesor
auth_bp.add_url_rule(
    "/register",
    endpoint="register",
    view_func=registrar_usuario,
    methods=["POST"]
)


# Registro anterior (compatibilidad)
auth_bp.add_url_rule(
    "/registro",
    endpoint="registro",
    view_func=registrar_usuario,
    methods=["POST"]
)


# Inicio de sesión con límite de intentos
auth_bp.add_url_rule(
    "/login",
    endpoint="login",
    view_func=limiter.limit("5 per minute")(iniciar_sesion),
    methods=["POST"]
)
