
# MuebleTech VES
# Sesión 2: Manejo de excepciones

from app.models.producto import Producto

try:
    mesa = Producto(
        codigo=2,
        nombre="Mesa industrial",
        precio=-450,
        stock=10,
        categoria="Mesas"
    )

    mesa.mostrar_informacion()

except ValueError as error:
    print("No se pudo registrar el producto.")
    print("Motivo:", error)
