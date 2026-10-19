
from flask import Blueprint, jsonify, request

# Crear el Blueprint para productos
productos_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/api/productos"
)

# Ruta de prueba
@productos_bp.route("/prueba", methods=["GET"])
def probar_blueprint():
    return jsonify({
        "mensaje": "Blueprint de MuebleTech VES funcionando"
    }), 200


# Importar la lista compartida de productos
from app.services.productos_data import productos

# GET: Consultar todos los productos
@productos_bp.route("", methods=["GET"])
def listar_productos():
    return jsonify({
        "mensaje": "Listado de productos",
        "total": len(productos),
        "productos": productos
    }), 200



# POST: Registrar un nuevo producto
@productos_bp.route("", methods=["POST"])
def registrar_producto():

    datos = request.get_json(silent=True)

    # Verificar que se reciba un JSON válido
    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar campos obligatorios
    campos = ["codigo", "nombre", "precio", "stock", "categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Validar los datos utilizando nuestra clase Producto
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
        return jsonify({"mensaje": str(error)}), 400

    # Verificar que el código no exista
    if any(p["codigo"] == nuevo.codigo for p in productos):
        return jsonify({
            "mensaje": "Ya existe un producto con ese código"
        }), 409

    # Preparar el nuevo producto
    producto_guardado = {
        "codigo": nuevo.codigo,
        "nombre": nuevo.nombre,
        "precio": nuevo.precio,
        "stock": nuevo.stock,
        "categoria": nuevo.categoria
    }

    # Guardarlo en nuestra lista compartida
    productos.append(producto_guardado)

    return jsonify({
        "mensaje": "Producto registrado correctamente",
        "producto": producto_guardado
    }), 201



# PUT: Actualizar un producto existente
@productos_bp.route("/<int:codigo>", methods=["PUT"])
def actualizar_producto(codigo):

    # Buscar el producto por su código
    producto_existente = next(
        (p for p in productos if p["codigo"] == codigo),
        None
    )

    if producto_existente is None:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    # Recibir los datos enviados por Postman
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # Verificar los campos obligatorios
    campos = ["nombre", "precio", "stock", "categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Validar los datos con nuestra clase Producto
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

    # Actualizar los datos
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



# DELETE: Eliminar un producto
@productos_bp.route("/<int:codigo>", methods=["DELETE"])
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

