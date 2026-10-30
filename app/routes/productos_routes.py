
# Proyecto: MuebleTech VES
# Rutas de productos con Flask Blueprints y control de roles

from flask import Blueprint, jsonify

from app.controllers.productos_controller import (
    listar_productos,
    registrar_producto,
    actualizar_producto,
    eliminar_producto
)

from app.services.autorizacion_service import (
    editor_required,
    admin_required
)


productos_bp = Blueprint(
    "productos_bp",
    __name__,
    url_prefix="/api/productos"
)


# GET: Ruta de prueba
@productos_bp.route("/prueba", methods=["GET"])
def probar_blueprint():
    return jsonify({
        "mensaje": "Blueprint de MuebleTech VES funcionando"
    }), 200


# GET: Consultar productos
# Acceso público (incluye usuarios CONSULTA)
productos_bp.add_url_rule(
    "",
    endpoint="listar_productos",
    view_func=listar_productos,
    methods=["GET"]
)


# POST: Registrar productos
# Solo EDITOR y ADMIN
productos_bp.add_url_rule(
    "",
    endpoint="registrar_producto",
    view_func=editor_required(registrar_producto),
    methods=["POST"]
)


# PUT: Actualizar productos
# Solo EDITOR y ADMIN
productos_bp.add_url_rule(
    "/<int:codigo>",
    endpoint="actualizar_producto",
    view_func=editor_required(actualizar_producto),
    methods=["PUT"]
)


# DELETE: Eliminar productos
# Solo ADMIN
productos_bp.add_url_rule(
    "/<int:codigo>",
    endpoint="eliminar_producto",
    view_func=admin_required(eliminar_producto),
    methods=["DELETE"]
)
