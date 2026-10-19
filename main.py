
# Proyecto: MuebleTech VES
# Sesión 3: API con Flask - Método GET

from flask import Flask, jsonify
from app.routes.productos_routes import productos_bp


# Crear aplicación Flask
app = Flask(__name__)
# Registrar las rutas del Blueprint
app.register_blueprint(productos_bp)


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
