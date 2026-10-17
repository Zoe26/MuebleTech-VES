
from app.models.mueble_industrial import MuebleIndustrial

mesa = MuebleIndustrial(
    codigo=3,
    nombre="Mesa industrial de comedor",
    precio=850.00,
    stock=5,
    categoria="Mesas",
    material="Madera y acero",
    dimensiones="180 x 90 x 75 cm"
)

mesa.mostrar_informacion()

