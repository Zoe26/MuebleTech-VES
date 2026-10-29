
from flask import Blueprint
from app.extensions import limiter

from app.controllers.auth_controller import (
    registrar_usuario,
    iniciar_sesion
)

# Blueprint para las rutas de autenticación
auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


# Endpoint para registrar usuarios
auth_bp.add_url_rule(
    "/registro",
    endpoint="registrar_usuario",
    view_func=registrar_usuario,
    methods=["POST"]
)




# Limitar los intentos de inicio de sesión
auth_bp.add_url_rule(
    "/login",
    endpoint="iniciar_sesion",
    view_func=limiter.limit("5 per minute")(iniciar_sesion),
    methods=["POST"]
)
