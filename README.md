# MuebleTech VES

## 1. Descripción del proyecto

**MuebleTech VES** es un proyecto de desarrollo Back End orientado a la gestión de un catálogo de muebles industriales del Parque Industrial de Villa El Salvador, Lima, Perú.

El sistema permite registrar, consultar, actualizar y eliminar productos mediante una **API REST desarrollada con Python y Flask**, aplicando programación orientada a objetos, validaciones de datos, manejo de errores HTTP y una arquitectura modular basada en Blueprints y Controllers.

El proyecto se desarrolla progresivamente como parte del curso de Programación Back End, incorporando nuevas funcionalidades durante las ocho sesiones.

## 2. Objetivo general

Desarrollar una API REST que permita gestionar la información de muebles industriales mediante operaciones CRUD, utilizando Python y Flask, con una arquitectura modular, documentación OpenAPI/Swagger y pruebas de endpoints, preparando su posterior integración con PostgreSQL y mecanismos de autenticación y seguridad.

## 3. Tecnologías utilizadas

| Tecnología | Descripción | Estado |
|---|---|---|
| Python 3.14.8 | Lenguaje de programación | Implementado |
| Flask 3.1.3 | Framework para desarrollar la API REST | Implementado |
| Flask Blueprints | Organización modular de rutas | Implementado |
| Flasgger 0.9.7.1 | Documentación Swagger/OpenAPI | Implementado |
| Postman | Pruebas de solicitudes HTTP | Implementado |
| Thunder Client | Pruebas HTTP desde Visual Studio Code | Implementado |
| Git y GitHub | Control de versiones | Implementado |
| PostgreSQL | Base de datos relacional | Pendiente |
| SQLAlchemy | ORM para persistencia de datos | Pendiente |
| JWT | Autenticación y protección de endpoints | Pendiente |

## 4. Funcionalidades implementadas

La API permite realizar las siguientes operaciones:

| Método HTTP | Endpoint | Descripción |
|---|---|---|
| GET | `/api/productos` | Consultar todos los productos |
| POST | `/api/productos` | Registrar un producto |
| PUT | `/api/productos/{codigo}` | Actualizar un producto existente |
| DELETE | `/api/productos/{codigo}` | Eliminar un producto |
| GET | `/api/productos/prueba` | Verificar el funcionamiento del Blueprint |

La API devuelve respuestas en formato JSON y utiliza códigos de estado HTTP como 200, 201, 400, 404 y 409.

## 5. Arquitectura del proyecto

MuebleTech VES utiliza una organización modular que separa las responsabilidades de la aplicación.

```text
MuebleTech-VES/
├── .vscode/
│   └── launch.json
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── productos_controller.py
│   ├── models/
│   │   ├── producto.py
│   │   ├── mueble_industrial.py
│   │   ├── categoria.py
│   │   └── usuario.py
│   ├── routes/
│   │   └── productos_routes.py
│   ├── services/
│   │   └── productos_data.py
│   ├── excepciones.py
│   └── __init__.py
├── docs/
│   └── swagger/
│       ├── productos_get.yml
│       ├── productos_post.yml
│       ├── productos_put.yml
│       └── productos_delete.yml
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Responsabilidades

- **main.py:** configura Flask, registra los Blueprints y define middlewares y manejadores de errores.
- **routes:** registra los endpoints mediante Flask Blueprints.
- **controllers:** procesa las solicitudes y genera respuestas HTTP.
- **models:** contiene las clases y validaciones del dominio del negocio.
- **services:** contiene actualmente el almacenamiento temporal de productos.
- **docs/swagger:** contiene los archivos YAML de documentación de la API.
- **tests:** contiene los ejercicios y pruebas desarrollados durante el curso.

## 6. Validaciones y manejo de errores

La aplicación incorpora validaciones mediante la clase `Producto`, incluyendo la verificación de campos obligatorios y restricciones sobre los datos.

También contempla respuestas para situaciones como:

- **400 Bad Request:** datos inválidos o campos obligatorios faltantes.
- **404 Not Found:** producto o ruta no encontrada.
- **409 Conflict:** intento de registrar un código de producto duplicado.
- **500 Internal Server Error:** error interno del servidor.

Se implementaron además los mecanismos `before_request` y `after_request` para registrar solicitudes HTTP y agregar un encabezado personalizado a las respuestas.

## 7. Documentación OpenAPI/Swagger

La API utiliza Flasgger para visualizar su documentación interactiva.

Con Flask ejecutándose, acceder desde