
# Proyecto: MuebleTech VES
# Controladores de productos

from flask import jsonify, request
from app.services.productos_data import productos
from flasgger import swag_from
from pathlib import Path


# Documentación Swagger de GET
@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_get.yml"
    )
)
# Controller GET: Consultar todos los productos
def listar_productos():
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
# Controller POST: Registrar un producto
def registrar_producto():

    # Recibir los datos enviados desde Thunder Client
    datos = request.get_json(silent=True)

    # Verificar que se reciba un objeto JSON
    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar los campos obligatorios
    campos = ["codigo", "nombre", "precio", "stock", "categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Utilizar nuestro modelo Producto
    from app.models.producto import Producto

    try:
        nuevo = Producto(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"],
            categoria=datos["categoria"]
        )
    except ValueError as error:
        return jsonify({
            "mensaje": str(error)
        }), 400

    # Verificar que el código no esté registrado
    if any(p["codigo"] == nuevo.codigo for p in productos):
        return jsonify({
            "mensaje": "Ya existe un producto con ese código"
        }), 409

    # Preparar el producto para almacenarlo
    producto_guardado = {
        "codigo": nuevo.codigo,
        "nombre": nuevo.nombre,
        "precio": nuevo.precio,
        "stock": nuevo.stock,
        "categoria": nuevo.categoria
    }

    # Registrar el producto
    productos.append(producto_guardado)

    return jsonify({
        "mensaje": "Producto registrado correctamente",
        "producto": producto_guardado
    }), 201




@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_put.yml"
    )
)
# Controller PUT: Actualizar un producto
def actualizar_producto(codigo):

    # Buscar el producto por su código
    producto_existente = next(
        (p for p in productos if p["codigo"] == codigo),
        None
    )

    # Verificar si existe
    if producto_existente is None:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    # Recibir los datos enviados por el cliente
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar campos obligatorios
    campos = ["nombre", "precio", "stock", "categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Validar utilizando nuestra clase Producto
    from app.models.producto import Producto

    try:
        producto_actualizado = Producto(
            codigo=codigo,
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"],
            categoria=datos["categoria"]
        )
    except ValueError as error:
        return jsonify({
            "mensaje": str(error)
        }), 400

    # Actualizar los datos del producto
    producto_existente.update({
        "nombre": producto_actualizado.nombre,
        "precio": producto_actualizado.precio,
        "stock": producto_actualizado.stock,
        "categoria": producto_actualizado.categoria
    })

    return jsonify({
        "mensaje": "Producto actualizado correctamente",
        "producto": producto_existente
    }), 200



@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "productos_delete.yml"
    )
)
# Controller DELETE: Eliminar un producto
def eliminar_producto(codigo):

    # Buscar el producto por su código
    producto_existente = next(
        (p for p in productos if p["codigo"] == codigo),
        None
    )

    # Verificar si existe
    if producto_existente is None:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    # Eliminar el producto
    productos.remove(producto_existente)

    return jsonify({
        "mensaje": "Producto eliminado correctamente",
        "codigo": codigo
    }), 200
