
# MuebleTech VES
# Sesión 2: Clase Categoria

class Categoria:

    def __init__(self, codigo, nombre, descripcion):

        # Validar código
        if type(codigo) is not int or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo")

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la categoría es obligatorio")

        # Validar descripción
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser un texto")

        # Guardar atributos
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()

    def mostrar_informacion(self):
        print("===== INFORMACIÓN DE LA CATEGORÍA =====")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
