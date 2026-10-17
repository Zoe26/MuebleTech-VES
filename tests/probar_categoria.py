
# MuebleTech VES
# Prueba de la clase Categoria

from app.models.categoria import Categoria

categoria = Categoria(
    codigo=1,
    nombre="Mesas industriales",
    descripcion="Mesas fabricadas con madera y estructuras metálicas"
)

categoria.mostrar_informacion()
