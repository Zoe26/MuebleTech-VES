
# Proyecto: MuebleTech VES
# Controladores de productos
# Autorización JWT y roles aplicada desde productos_routes.py

from pathlib import Path

from flask import jsonify, request
from flasgger import swag_from

from app.extensions import db
from app.models.producto import Producto
from app.models.producto_db import ProductoDB
from app.models.categoria_db import CategoriaDB


# =========================================================
# GET: CONSULTAR PRODUCTOS
# Acceso público
# Permite filtrar mediante ?categoria=1
# =========================================================

@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_get.yml"
    )
)
def listar_productos():

    # Obtener el filtro opcional de categoría
    categoria = request.args.get("categoria")

    # Construir la consulta de productos
    consulta = db.select(ProductoDB)

    # Validar y aplicar el filtro de categoría
    if categoria is not None:

        if not categoria.isdigit() or int(categoria) <= 0:
            return jsonify({
                "error": "La categoría debe ser un entero positivo"
            }), 400

        consulta = consulta.where(
            ProductoDB.id_categoria == int(categoria)
        )

    # Consultar los productos en PostgreSQL
    registros = db.session.execute(
        consulta.order_by(ProductoDB.codigo)
    ).scalars().all()

    productos = []

    for p in registros:
        productos.append({
            "codigo": p.codigo,
            "nombre": p.nombre,
            "precio": float(p.precio),
            "stock": p.stock,
            "id_categoria": p.id_categoria,
            "categoria": p.categoria.nombre
        })

    return jsonify({
        "mensaje": "Listado de productos",
        "total": len(productos),
        "productos": productos
    }), 200


# =========================================================
# POST: REGISTRAR UN PRODUCTO
# Permitido para EDITOR y ADMIN desde las rutas
# =========================================================

@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_post.yml"
    )
)
def registrar_producto():

    # Obtener los datos enviados en formato JSON
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "error": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar campos obligatorios
    campos = ["nombre", "precio", "stock", "id_categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "error": f"Falta el campo: {campo}"
            }), 400

    # Validar el identificador de categoría
    id_categoria = datos["id_categoria"]

    if type(id_categoria) is not int or id_categoria <= 0:
        return jsonify({
            "error": "id_categoria debe ser un entero positivo"
        }), 400

    # Verificar que la categoría exista
    categoria = db.session.get(CategoriaDB, id_categoria)

    if categoria is None:
        return jsonify({
            "error": "La categoría indicada no existe"
        }), 400

    # Validar los datos mediante la clase Producto
    try:
        producto_validado = Producto(
            codigo=1,
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"],
            categoria=categoria.nombre
        )

    except (ValueError, TypeError) as error:
        return jsonify({
            "error": str(error)
        }), 400

    # Crear el registro en PostgreSQL
    nuevo = ProductoDB(
        nombre=producto_validado.nombre,
        precio=producto_validado.precio,
        stock=producto_validado.stock,
        id_categoria=id_categoria
    )

    try:
        db.session.add(nuevo)
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "No se pudo registrar el producto"
        }), 500

    return jsonify({
        "mensaje": "Producto registrado correctamente",
        "producto": {
            "codigo": nuevo.codigo,
            "nombre": nuevo.nombre,
            "precio": float(nuevo.precio),
            "stock": nuevo.stock,
            "id_categoria": nuevo.id_categoria,
            "categoria": categoria.nombre
        }
    }), 201


# =========================================================
# PUT: ACTUALIZAR UN PRODUCTO
# Permitido para EDITOR y ADMIN desde las rutas
# =========================================================

@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_put.yml"
    )
)
def actualizar_producto(codigo):

    # Buscar el producto en PostgreSQL
    producto = db.session.get(ProductoDB, codigo)

    if producto is None:
        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    # Obtener los datos enviados en formato JSON
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "error": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar campos obligatorios
    campos = ["nombre", "precio", "stock", "id_categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "error": f"Falta el campo: {campo}"
            }), 400

    # Validar el identificador de categoría
    id_categoria = datos["id_categoria"]

    if type(id_categoria) is not int or id_categoria <= 0:
        return jsonify({
            "error": "id_categoria debe ser un entero positivo"
        }), 400

    # Verificar que la categoría exista
    categoria = db.session.get(CategoriaDB, id_categoria)

    if categoria is None:
        return jsonify({
            "error": "La categoría indicada no existe"
        }), 400

    # Validar mediante la clase Producto existente
    try:
        producto_validado = Producto(
            codigo=codigo,
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"],
            categoria=categoria.nombre
        )

    except (ValueError, TypeError) as error:
        return jsonify({
            "error": str(error)
        }), 400

    # Actualizar los datos del producto
    producto.nombre = producto_validado.nombre
    producto.precio = producto_validado.precio
    producto.stock = producto_validado.stock
    producto.id_categoria = id_categoria

    try:
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "No se pudo actualizar el producto"
        }), 500

    return jsonify({
        "mensaje": "Producto actualizado correctamente",
        "producto": {
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio": float(producto.precio),
            "stock": producto.stock,
            "id_categoria": producto.id_categoria,
            "categoria": categoria.nombre
        }
    }), 200


# =========================================================
# DELETE: ELIMINAR UN PRODUCTO
# Permitido únicamente para ADMIN desde las rutas
# =========================================================

@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_delete.yml"
    )
)
def eliminar_producto(codigo):

    # Buscar el producto en PostgreSQL
    producto = db.session.get(ProductoDB, codigo)

    if producto is None:
        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    # Guardar los datos antes de eliminar
    datos_producto = {
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "precio": float(producto.precio),
        "stock": producto.stock,
        "id_categoria": producto.id_categoria
    }

    try:
        db.session.delete(producto)
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "No se pudo eliminar el producto"
        }), 500

    return jsonify({
        "mensaje": "Producto eliminado correctamente",
        "producto": datos_producto
    }), 200
