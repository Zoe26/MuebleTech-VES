
# Proyecto: MuebleTech VES
# Sesión 4: API REST con Blueprints y Middlewares

from flask import Flask, jsonify, request
from app.routes.productos_routes import productos_bp
from app.routes.categorias_routes import categorias_bp
from flasgger import Swagger
from config import Config
from app.extensions import db, migrate, bcrypt, jwt, cors, limiter
from app.models.categoria_db import CategoriaDB
from app.models.producto_db import ProductoDB
from app.models.usuario_db import UsuarioDB
from app.routes.auth_routes import auth_bp

app = Flask(__name__)

app.config.from_object(Config)

# Inicializar las extensiones
db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
jwt.init_app(app)

cors.init_app(
    app,
    resources={
        r"/api/*": {
            "origins": app.config["CORS_ORIGINS"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    }
)

limiter.init_app(app)


# Registrar las rutas del Blueprint
app.register_blueprint(productos_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(auth_bp)



# Configuración de seguridad para Swagger
swagger_config = {
    "swagger": "2.0",
    "info": {
        "title": "MuebleTech VES API",
        "version": "1.0.0",
        "description": "API REST para la gestión de muebles industriales"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": (
                "Ingrese: Bearer seguido de un espacio "
                "y su token JWT."
            )
        }
    }
}

swagger = Swagger(app, template=swagger_config)



# Middleware básico: registrar las solicitudes HTTP
@app.before_request
def registrar_solicitud():
    print(f"Solicitud recibida: {request.method} {request.path}")



# Middleware básico: agregar encabezados HTTP
@app.after_request
def agregar_encabezados(response):

    # Identificar nuestra aplicación en las respuestas
    response.headers["X-Proyecto"] = "MuebleTech VES"

    return response


# Manejo de errores HTTP: ruta no encontrada
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return jsonify({
        "mensaje": "La ruta solicitada no existe",
        "codigo": 404
    }), 404


# Manejo de errores HTTP: error interno del servidor
@app.errorhandler(500)
def error_interno(error):
    return jsonify({
        "mensaje": "Ocurrió un error interno en el servidor",
        "codigo": 500
    }), 500


# Manejo de errores HTTP 429:
# demasiadas solicitudes al servidor
@app.errorhandler(429)
def demasiadas_solicitudes(error):
    return jsonify({
        "mensaje": "Demasiados intentos. Intente nuevamente más tarde.",
        "codigo": 429
    }), 429


# Ruta principal
@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "proyecto": "MuebleTech VES",
        "mensaje": "Bienvenido a nuestra API REST",
        "estado": "funcionando"
    }), 200


# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)



