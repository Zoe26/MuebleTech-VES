
# MuebleTech VES
# Prueba de la clase Usuario

from app.models.usuario import Usuario

usuario = Usuario(
    codigo=1,
    nombre="Administrador MuebleTech",
    correo="admin@example.com",
    rol="administrador"
)

usuario.mostrar_informacion()
