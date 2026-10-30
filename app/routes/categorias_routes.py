
# Proyecto: MuebleTech VES
# Rutas de categorías y autorización por roles
# Documentación Swagger para GET, POST, PUT y DELETE

from pathlib import Path

from flask import Blueprint, request
from flasgger import swag_from

from app.controllers.categorias_controller import (
    listar_categorias,
    registrar_categoria,
    actualizar_categoria,
    eliminar_categoria
)

from app.services.autorizacion_service import (
    editor_required,
    admin_required
)


# =========================================================
# BLUEPRINT DE CATEGORÍAS
# =========================================================

categorias_bp = Blueprint(
    "categorias_bp",
    __name__,
    url_prefix="/api/categorias"
)


# =========================================================
# GET: CONSULTAR CATEGORÍAS
# Acceso público
# =========================================================

@categorias_bp.route("", methods=["GET"])
@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "categorias_get.yml"
    )
)
def obtener_categorias():
    return listar_categorias()


# =========================================================
# POST: REGISTRAR CATEGORÍA
# Permitido para EDITOR y ADMIN
# =========================================================

@categorias_bp.route("", methods=["POST"])
@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "categorias_post.yml"
    )
)
@editor_required
def crear_categoria():
    datos = request.get_json(silent=True)
    return registrar_categoria(datos)


# =========================================================
# PUT: ACTUALIZAR CATEGORÍA
# Permitido para EDITOR y ADMIN
# =========================================================

@categorias_bp.route("/<int:id_categoria>", methods=["PUT"])
@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "categorias_put.yml"
    )
)
@editor_required
def editar_categoria(id_categoria):
    datos = request.get_json(silent=True)
    return actualizar_categoria(id_categoria, datos)


# =========================================================
# DELETE: ELIMINAR CATEGORÍA
# Permitido únicamente para ADMIN
# =========================================================

@categorias_bp.route("/<int:id_categoria>", methods=["DELETE"])
@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "categorias_delete.yml"
    )
)
@admin_required
def borrar_categoria(id_categoria):
    return eliminar_categoria(id_categoria)
