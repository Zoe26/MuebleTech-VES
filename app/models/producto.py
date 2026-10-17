
# MuebleTech VES
# Sesión 2: Validaciones de la clase Producto

from app.excepciones import PrecioInvalidoError, StockInvalidoError


class Producto:

    def __init__(self, codigo, nombre, precio, stock, categoria):

        # Validar código
        if type(codigo) is not int or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo")

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        # Validar precio
        
        if type(precio) not in (int, float) or precio <= 0:
            raise PrecioInvalidoError("El precio debe ser mayor que cero")


        # Validar stock       
        if type(stock) is not int or stock < 0:
            raise StockInvalidoError("El stock debe ser un entero no negativo")


        # Validar categoría
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía")

        # Guardar los datos validados
        self.codigo = codigo
        self.nombre = nombre.strip()
        self._precio = precio
        self.stock = stock
        self.categoria = categoria.strip()
        
        
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if type(nuevo_precio) not in (int, float) or nuevo_precio <= 0:
            raise PrecioInvalidoError("El precio debe ser mayor que cero")

        self._precio = nuevo_precio

        
    def mostrar_informacion(self):
        print("===== INFORMACIÓN DEL PRODUCTO =====")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Precio: S/", self.precio)
        print("Stock:", self.stock)
        print("Categoría:", self.categoria)
