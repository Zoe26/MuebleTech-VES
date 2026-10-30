
# Proyecto: MuebleTech VES
# Punto de entrada de la API REST
# Arquitectura App Factory

from app import create_app


# Crear la aplicación Flask
app = create_app()


# Ejecutar solamente en desarrollo local
if __name__ == "__main__":
    app.run(debug=True)
