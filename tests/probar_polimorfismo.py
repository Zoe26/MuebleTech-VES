
# MuebleTech VES
# Sesión 2: Polimorfismo

from app.models.producto import Producto
from app.models.mueble_industrial import MuebleIndustrial

# Objeto de la clase padre
producto = Producto(
    codigo=1,
    nombre="Silla básica",
    precio=150.00,
    stock=20,
    categoria="Sillas"
)

# Objeto de la clase hija
mueble = MuebleIndustrial(
    codigo=2,
    nombre="Mesa industrial",
    precio=850.00,
    stock=5,
    categoria="Mesas",
    material="Madera y acero",
    dimensiones="180 x 90 x 75 cm"
)

# Aplicamos polimorfismo
for item in [producto, mueble]:
    item.mostrar_informacion()
    print("---------------------------")
