
# MuebleTech VES
# Sesión 2: Prueba de encapsulamiento

from app.models.producto import Producto

# Crear un producto válido
mesa = Producto(
    codigo=1,
    nombre="Mesa industrial",
    precio=450.00,
    stock=10,
    categoria="Mesas"
)

print("Precio inicial: S/", mesa.precio)

# Modificar el precio correctamente
mesa.precio = 500.00

print("Precio actualizado: S/", mesa.precio)

# Intentar asignar un precio negativo
try:
    mesa.precio = -200

except ValueError as error:
    print("No se pudo actualizar el precio.")
    print("Motivo:", error)

# Comprobar que se conserva el último precio válido
print("Precio final: S/", mesa.precio)
