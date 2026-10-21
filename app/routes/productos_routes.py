
# Proyecto: MuebleTech VES
# Sesión 4: Rutas de productos con Flask Blueprints

from flask import Blueprint, jsonify

from app.controllers.productos_controller import (
    listar_productos,
    registrar_producto,
    actualizar_producto,
    eliminar_producto
)

# Crear el Blueprint para productos
productos_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/api/productos"
)

# Ruta de prueba del Blueprint
@productos_bp.route("/prueba", methods=["GET"])
def probar_blueprint():
    return jsonify({
        "mensaje": "Blueprint de MuebleTech VES funcionando"
    }), 200


# GET: Consultar productos
productos_bp.add_url_rule(
    "",
    endpoint="listar_productos",
    view_func=listar_productos,
    methods=["GET"]
)

# POST: Registrar productos
productos_bp.add_url_rule(
    "",
    endpoint="registrar_producto",
    view_func=registrar_producto,
    methods=["POST"]
)

# PUT: Actualizar productos
productos_bp.add_url_rule(
    "/<int:codigo>",
    endpoint="actualizar_producto",
    view_func=actualizar_producto,
    methods=["PUT"]
)

# DELETE: Eliminar productos
productos_bp.add_url_rule(
    "/<int:codigo>",
    endpoint="eliminar_producto",
    view_func=eliminar_producto,
    methods=["DELETE"]
)
