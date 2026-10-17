
# MuebleTech VES
# Sesión 2: Herencia

from app.models.producto import Producto


class MuebleIndustrial(Producto):

    def __init__(self, codigo, nombre, precio, stock,
                 categoria, material, dimensiones):

        # Inicializar los atributos de la clase padre
        super().__init__(
            codigo, nombre, precio, stock, categoria
        )

        # Atributos propios de MuebleIndustrial
        self.material = material
        self.dimensiones = dimensiones

    
    # Polimorfismo: sobrescribimos el método heredado
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Material:", self.material)
        print("Dimensiones:", self.dimensiones)
