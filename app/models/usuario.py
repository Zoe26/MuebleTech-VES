
# MuebleTech VES
# Sesión 2: Clase Usuario

class Usuario:

    def __init__(self, codigo, nombre, correo, rol):

        # Validar código
        if type(codigo) is not int or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo")

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio")

        # Validar correo
        if not isinstance(correo, str) or (
            "@" not in correo or "." not in correo.split("@")[-1]
        ):
            raise ValueError("El correo electrónico no es válido")

        # Validar rol
        if rol not in ("administrador", "usuario"):
            raise ValueError("El rol debe ser administrador o usuario")

        # Guardar atributos
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.rol = rol

    def mostrar_informacion(self):
        print("===== INFORMACIÓN DEL USUARIO =====")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Correo:", self.correo)
        print("Rol:", self.rol)
