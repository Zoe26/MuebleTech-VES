
# Proyecto: MuebleTech VES
# Sesión 4: API REST con Blueprints y Middlewares

from flask import Flask, jsonify, request
from app.routes.productos_routes import productos_bp
from flasgger import Swagger
from config import Config
from app.extensions import db, migrate
# Modelos de PostgreSQL
from app.models.categoria_db import CategoriaDB
from app.models.producto_db import ProductoDB



# Crear aplicación Flask
app = Flask(__name__)


# Configurar conexión con PostgreSQL
app.config.from_object(Config)

# Inicializar SQLAlchemy
db.init_app(app)

# Inicializar Flask-Migrate
migrate.init_app(app, db)


# Registrar las rutas del Blueprint
app.register_blueprint(productos_bp)


# Configurar Swagger para documentar nuestra API REST
swagger = Swagger(app)



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
