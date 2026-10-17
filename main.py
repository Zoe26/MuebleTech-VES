
# Proyecto: MuebleTech VES
# Sesión 3: API con Flask - Método GET

from flask import Flask, jsonify, request

# Crear aplicación Flask
app = Flask(__name__)


# Ruta principal
@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "proyecto": "MuebleTech VES",
        "mensaje": "Bienvenido a nuestra API REST",
        "estado": "funcionando"
    }), 200


# Lista temporal de productos
productos = [
    {
        "codigo": 1,
        "nombre": "Mesa industrial",
        "precio": 450.00,
        "stock": 10,
        "categoria": "Mesas"
    },
    {
        "codigo": 2,
        "nombre": "Silla industrial",
        "precio": 150.00,
        "stock": 20,
        "categoria": "Sillas"
    },
    {
        "codigo": 3,
        "nombre": "Sala industrial",
        "precio": 650.00,
        "stock": 5,
        "categoria": "Salas"
    }
]


# Endpoint GET: Consultar todos los productos
@app.route("/api/productos", methods=["GET"])
def listar_productos():
    return jsonify({
        "mensaje": "Listado de productos",
        "total": len(productos),
        "productos": productos
    }), 200


# Endpoint POST: Registrar un nuevo producto
@app.route("/api/productos", methods=["POST"])
def registrar_producto():

    # Recibir el JSON enviado por el cliente
    datos = request.get_json(silent=True)

    # Verificar que se reciba un objeto JSON
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

    # Importar nuestra clase Producto
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

    # Comprobar si el código ya existe
    if any(p["codigo"] == nuevo.codigo for p in productos):
        return jsonify({
            "mensaje": "Ya existe un producto con ese código"
        }), 409

    # Convertir el objeto en un diccionario
    producto_guardado = {
        "codigo": nuevo.codigo,
        "nombre": nuevo.nombre,
        "precio": nuevo.precio,
        "stock": nuevo.stock,
        "categoria": nuevo.categoria
    }

    # Agregarlo a nuestra lista temporal
    productos.append(producto_guardado)

    return jsonify({
        "mensaje": "Producto registrado correctamente",
        "producto": producto_guardado
    }), 201


# Endpoint PUT: Actualizar un producto existente
@app.route("/api/productos/<int:codigo>", methods=["PUT"])
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

    # Verificar que todos los campos estén presentes
    campos = ["nombre", "precio", "stock", "categoria"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # Validar los nuevos datos con nuestra clase Producto
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

    # Actualizar los datos en nuestra lista temporal
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


# Endpoint DELETE: Eliminar un producto
@app.route("/api/productos/<int:codigo>", methods=["DELETE"])
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

    # Eliminar el producto de la lista temporal
    productos.remove(producto_existente)

    return jsonify({
        "mensaje": "Producto eliminado correctamente",
        "codigo": codigo
    }), 200

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)
