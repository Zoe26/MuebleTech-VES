
from flask import jsonify
from app.extensions import db
from app.models.categoria_db import CategoriaDB
from app.models.producto_db import ProductoDB

def listar_categorias():
    """Obtiene todas las categorías registradas."""

    categorias = db.session.query(CategoriaDB).order_by(
        CategoriaDB.id_categoria
    ).all()

    resultado = [
        {
            "id_categoria": categoria.id_categoria,
            "nombre": categoria.nombre,
            "descripcion": categoria.descripcion
        }
        for categoria in categorias
    ]

    return jsonify({
        "mensaje": "Listado de categorías",
        "categorias": resultado,
        "total": len(resultado)
    }), 200



def registrar_categoria(datos):
    """Registra una nueva categoría en PostgreSQL."""

    if not isinstance(datos, dict):
        return jsonify({"error": "Debes enviar un objeto JSON"}), 400

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion")

    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({"error": "El nombre es obligatorio"}), 400

    nombre = nombre.strip()

    if len(nombre) > 100:
        return jsonify({"error": "El nombre no puede superar 100 caracteres"}), 400

    if descripcion is not None and not isinstance(descripcion, str):
        return jsonify({"error": "La descripción debe ser texto"}), 400

    existente = CategoriaDB.query.filter(
        db.func.lower(CategoriaDB.nombre) == nombre.lower()
    ).first()

    if existente:
        return jsonify({"error": "La categoría ya existe"}), 409

    nueva_categoria = CategoriaDB(
        nombre=nombre,
        descripcion=descripcion.strip() if descripcion else None
    )

    try:
        db.session.add(nueva_categoria)
        db.session.commit()

        return jsonify({
            "mensaje": "Categoría registrada correctamente",
            "categoria": {
                "id_categoria": nueva_categoria.id_categoria,
                "nombre": nueva_categoria.nombre,
                "descripcion": nueva_categoria.descripcion
            }
        }), 201

    except Exception:
        db.session.rollback()
        return jsonify({"error": "No se pudo registrar la categoría"}), 500



# =========================================================
# PUT: ACTUALIZAR UNA CATEGORÍA
# Autorización gestionada desde categorias_routes.py
# =========================================================

def actualizar_categoria(id_categoria, datos):

    categoria = db.session.get(CategoriaDB, id_categoria)

    if categoria is None:
        return jsonify({
            "error": "Categoría no encontrada"
        }), 404

    if not isinstance(datos, dict):
        return jsonify({
            "error": "Debe enviar un objeto JSON válido"
        }), 400

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion")

    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({
            "error": "El nombre es obligatorio"
        }), 400

    nombre = nombre.strip()

    if len(nombre) > 100:
        return jsonify({
            "error": "El nombre supera los 100 caracteres"
        }), 400

    if descripcion is not None and not isinstance(descripcion, str):
        return jsonify({
            "error": "La descripción debe ser texto"
        }), 400

    existente = CategoriaDB.query.filter(
        db.func.lower(CategoriaDB.nombre) == nombre.lower(),
        CategoriaDB.id_categoria != id_categoria
    ).first()

    if existente:
        return jsonify({
            "error": "Ya existe otra categoría con ese nombre"
        }), 409

    categoria.nombre = nombre
    categoria.descripcion = (
        descripcion.strip() if descripcion else None
    )

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "No se pudo actualizar la categoría"
        }), 500

    return jsonify({
        "mensaje": "Categoría actualizada correctamente",
        "categoria": {
            "id_categoria": categoria.id_categoria,
            "nombre": categoria.nombre,
            "descripcion": categoria.descripcion
        }
    }), 200



# =========================================================
# DELETE: ELIMINAR UNA CATEGORÍA
# Autorización gestionada desde categorias_routes.py
# =========================================================

def eliminar_categoria(id_categoria):

    # Buscar la categoría en PostgreSQL
    categoria = db.session.get(CategoriaDB, id_categoria)

    if categoria is None:
        return jsonify({
            "error": "Categoría no encontrada"
        }), 404

    # Impedir eliminar categorías que tienen productos
    productos_asociados = db.session.query(ProductoDB).filter_by(
        id_categoria=id_categoria
    ).first()

    if productos_asociados is not None:
        return jsonify({
            "error": "No se puede eliminar una categoría con productos asociados"
        }), 409

    datos_categoria = {
        "id_categoria": categoria.id_categoria,
        "nombre": categoria.nombre,
        "descripcion": categoria.descripcion
    }

    try:
        db.session.delete(categoria)
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "No se pudo eliminar la categoría"
        }), 500

    return jsonify({
        "mensaje": "Categoría eliminada correctamente",
        "categoria": datos_categoria
    }), 200
