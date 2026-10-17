
# MuebleTech VES
# Sesión 2: Creación de objetos

from app.models.producto import Producto

# Creamos nuestro primer objeto
mesa = Producto(
    codigo=1,
    nombre="Mesa industrial",
    precio=450.00,
    stock=10,
    categoria="Mesas"
)

# Ejecutamos un método del objeto
mesa.mostrar_informacion()
