
# Proyecto: MuebleTech VES
# Controladores de productos

from flask import jsonify, request
from app.services.productos_data import productos
from flasgger import swag_from
from pathlib import Path
from app.models.producto_db import ProductoDB
from app.extensions import db
from app.models.categoria_db import CategoriaDB
from app.models.producto import Producto

# Documentación Swagger de GET
@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_get.yml"
    )
)
# Controller GET: Consultar todos los productos

def listar_productos():

    # Consultar los productos almacenados en PostgreSQL
    registros = db.session.execute(
        db.select(ProductoDB).order_by(ProductoDB.codigo)
    ).scalars().all()

    # Convertir los resultados en diccionarios
    productos = []

    for p in registros:
        productos.append({
            "codigo": p.codigo,
            "nombre": p.nombre,
            "precio": float(p.precio),
            "stock": p.stock,
            "categoria": p.categoria.nombre
        })

    return jsonify({
        "mensaje": "Listado de productos",
        "total": len(productos),
        "productos": productos
    }), 200



@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_post.yml"
    )
)
# Controller POST: Registrar producto en PostgreSQL
def registrar_producto():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # Campos requeridos
    campos = ["nombre", "precio", "stock", "id_categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Validar el identificador de categoría
    id_categoria = datos["id_categoria"]

    if type(id_categoria) is not int or id_categoria <= 0:
        return jsonify({
            "mensaje": "id_categoria debe ser un entero positivo"
        }), 400

    # Verificar que la categoría exista
    categoria = db.session.get(CategoriaDB, id_categoria)

    if categoria is None:
        return jsonify({
            "mensaje": "La categoría indicada no existe"
        }), 400

    # Conservar las validaciones de nuestra clase Producto
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
            "mensaje": str(error)
        }), 400

    # Crear el registro de PostgreSQL
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
            "mensaje": "No se pudo registrar el producto"
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


@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_put.yml"
    )
)
# Controller PUT: Actualizar un producto en PostgreSQL
def actualizar_producto(codigo):

    # Buscar el producto en PostgreSQL
    producto = db.session.get(ProductoDB, codigo)

    if producto is None:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    # Obtener el JSON enviado por el cliente
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar campos obligatorios
    campos = ["nombre", "precio", "stock", "id_categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Validar la categoría
    id_categoria = datos["id_categoria"]

    if type(id_categoria) is not int or id_categoria <= 0:
        return jsonify({
            "mensaje": "id_categoria debe ser un entero positivo"
        }), 400

    categoria = db.session.get(CategoriaDB, id_categoria)

    if categoria is None:
        return jsonify({
            "mensaje": "La categoría indicada no existe"
        }), 400

    # Validar los datos mediante nuestra clase Producto
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
            "mensaje": str(error)
        }), 400

    # Actualizar el producto
    producto.nombre = producto_validado.nombre
    producto.precio = producto_validado.precio
    producto.stock = producto_validado.stock
    producto.id_categoria = id_categoria

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({
            "mensaje": "No se pudo actualizar el producto"
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


@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_delete.yml"
    )
)
# Controller DELETE: Eliminar producto de PostgreSQL
def eliminar_producto(codigo):

    # 1. Buscar el producto por su código
    producto = db.session.get(ProductoDB, codigo)

    # 2. Comprobar si existe
    if producto is None:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    # 3. Guardar los datos antes de eliminarlo
    datos_producto = {
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "precio": float(producto.precio),
        "stock": producto.stock,
        "id_categoria": producto.id_categoria
    }

    # 4. Eliminar el producto de PostgreSQL
    try:
        db.session.delete(producto)
        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({
            "mensaje": "No se pudo eliminar el producto"
        }), 500

    # 5. Confirmar la eliminación
    return jsonify({
        "mensaje": "Producto eliminado correctamente",
        "producto": datos_producto
    }), 200
