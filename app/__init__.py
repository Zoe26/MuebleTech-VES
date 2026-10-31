
# Proyecto: MuebleTech VES
# Patrón de arquitectura App Factory

from flask import Flask, jsonify, request
from flasgger import Swagger

from app.extensions import (
    db,
    migrate,
    bcrypt,
    jwt,
    cors,
    limiter
)


def create_app():
    """Crea y configura la aplicación Flask."""

    app = Flask(__name__)

    # Configuración de PostgreSQL y JWT
    from config import Config
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    
    # Respuestas JSON uniformes para errores JWT

    @jwt.expired_token_loader
    def token_expirado(jwt_header, jwt_payload):
        return jsonify({
            "error": "El token ha expirado"
        }), 401

    @jwt.invalid_token_loader
    def token_invalido(motivo):
        return jsonify({
            "error": "Token inválido"
        }), 422

    @jwt.unauthorized_loader
    def token_ausente(motivo):
        return jsonify({
            "error": "Se requiere autenticación JWT"
        }), 401

    @jwt.revoked_token_loader
    def token_revocado(jwt_header, jwt_payload):
        return jsonify({
            "error": "Token revocado"
        }), 401

    @jwt.needs_fresh_token_loader
    def token_no_reciente(jwt_header, jwt_payload):
        return jsonify({
            "error": "Se requiere un token reciente"
        }), 401


    cors.init_app(
        app,
        resources={
            r"/api/*": {
                "origins": app.config["CORS_ORIGINS"],
                "methods": [
                    "GET", "POST", "PUT",
                    "DELETE", "OPTIONS"
                ],
                "allow_headers": [
                    "Content-Type", "Authorization"
                ]
            }
        }
    )

    limiter.init_app(app)

    # Registrar modelos ORM
    from app.models.categoria_db import CategoriaDB
    from app.models.producto_db import ProductoDB
    from app.models.usuario_db import UsuarioDB

    # Registrar Blueprints
    from app.routes.productos_routes import productos_bp
    from app.routes.categorias_routes import categorias_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(productos_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(auth_bp)

    # Documentación Swagger
    swagger_config = {
        "swagger": "2.0",
        "info": {
            "title": "MuebleTech VES API",
            "version": "1.0.0",
            "description": (
                "API REST para la gestión de muebles "
                "industriales con PostgreSQL, JWT "
                "y autorización por roles."
            )
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": (
                    "Ingrese Bearer seguido de un "
                    "espacio y su token JWT."
                )
            }
        }
    }

    Swagger(app, template=swagger_config)

    # Middleware de entrada
    @app.before_request
    def registrar_solicitud():
        app.logger.info(
            "Solicitud recibida: %s %s",
            request.method,
            request.path
        )

    # Middleware de salida
    @app.after_request
    def agregar_encabezados(response):
        response.headers["X-Proyecto"] = "MuebleTech VES"
        return response

    # Manejadores globales de errores
    @app.errorhandler(400)
    def solicitud_incorrecta(error):
        return jsonify({
            "error": "Solicitud incorrecta o datos inválidos"
        }), 400

    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return jsonify({
            "error": "La ruta solicitada no existe"
        }), 404

    @app.errorhandler(405)
    def metodo_no_permitido(error):
        return jsonify({
            "error": "Método HTTP no permitido"
        }), 405

    @app.errorhandler(429)
    def demasiadas_solicitudes(error):
        return jsonify({
            "error": "Demasiadas solicitudes. Intente más tarde."
        }), 429

    @app.errorhandler(500)
    def error_interno(error):
        db.session.rollback()

        app.logger.error(
            "Error interno durante la solicitud: %s",
            request.path,
            exc_info=True
        )

        return jsonify({
            "error": "Ocurrió un error interno en el servidor"
        }), 500

    # Ruta principal
    @app.route("/", methods=["GET"])
    def inicio():
        return jsonify({
            "proyecto": "MuebleTech VES",
            "mensaje": "Bienvenido a nuestra API REST",
            "estado": "funcionando"
        }), 200

    return app
