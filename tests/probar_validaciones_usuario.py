
# MuebleTech VES
# Sesión 2: Validaciones de Usuario

from app.models.usuario import Usuario

# Caso 1: Usuario sin nombre
try:
    usuario1 = Usuario(
        codigo=1,
        nombre="",
        correo="admin@example.com",
        rol="administrador"
    )
except ValueError as error:
    print("Caso 1:", error)


# Caso 2: Correo inválido
try:
    usuario2 = Usuario(
        codigo=2,
        nombre="Administrador",
        correo="correo_incorrecto",
        rol="administrador"
    )
except ValueError as error:
    print("Caso 2:", error)


# Caso 3: Rol no permitido
try:
    usuario3 = Usuario(
        codigo=3,
        nombre="Administrador",
        correo="admin@example.com",
        rol="superusuario"
    )
except ValueError as error:
    print("Caso 3:", error)
