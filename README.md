
# MuebleTech VES

## 1. Descripción del proyecto

**MuebleTech VES** es un proyecto de desarrollo Back End orientado a la gestión de un catálogo de muebles industriales del Parque Industrial de Villa El Salvador, Lima, Perú.

El sistema permite registrar, consultar, actualizar y eliminar productos mediante una **API REST desarrollada con Python y Flask**, aplicando programación orientada a objetos, validaciones de datos, manejo de errores HTTP y una arquitectura modular basada en Blueprints y Controllers.

A partir de la Sesión 5, la aplicación incorpora **persistencia de datos con PostgreSQL y Flask-SQLAlchemy**, permitiendo almacenar permanentemente los productos y relacionarlos con sus respectivas categorías.

El proyecto se desarrolla progresivamente como parte del curso de Programación Back End, incorporando nuevas funcionalidades durante ocho sesiones.

## 2. Objetivo general

Desarrollar una API REST que permita gestionar la información de muebles industriales mediante operaciones CRUD, utilizando Python y Flask, con una arquitectura modular, documentación OpenAPI/Swagger y persistencia de datos en PostgreSQL mediante Flask-SQLAlchemy.

El proyecto contempla posteriormente la incorporación de mecanismos de autenticación y seguridad, así como su despliegue en un entorno de producción.

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
| PostgreSQL 17 | Base de datos relacional | Implementado |
| pgAdmin 4 | Administración de PostgreSQL | Implementado |
| Flask-SQLAlchemy | ORM para persistencia de datos | Implementado |
| Flask-Migrate | Gestión de migraciones de base de datos | Implementado |
| psycopg | Conector de Python con PostgreSQL | Implementado |
| python-dotenv | Gestión de variables de entorno | Implementado |
| JWT | Autenticación y protección de endpoints | Pendiente - Sesión 6 |

## 4. Funcionalidades implementadas

La API permite realizar las siguientes operaciones:

| Método HTTP | Endpoint | Descripción |
|---|---|---|
| GET | `/api/productos` | Consultar todos los productos almacenados en PostgreSQL |
| POST | `/api/productos` | Registrar un nuevo producto |
| PUT | `/api/productos/{codigo}` | Actualizar un producto existente |
| DELETE | `/api/productos/{codigo}` | Eliminar un producto |
| GET | `/api/productos/prueba` | Verificar el funcionamiento del Blueprint |

La API devuelve respuestas en formato JSON y utiliza códigos de estado HTTP como 200, 201, 400, 404 y 500.

Las operaciones CRUD principales utilizan Flask-SQLAlchemy para interactuar con PostgreSQL, garantizando que los cambios se mantengan almacenados después de reiniciar la aplicación.

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
│   │   ├── usuario.py
│   │   ├── categoria_db.py
│   │   └── producto_db.py
│   ├── routes/
│   │   └── productos_routes.py
│   ├── services/
│   │   └── productos_data.py
│   ├── extensions.py
│   ├── excepciones.py
│   └── __init__.py
├── docs/
│   └── swagger/
│       ├── productos_get.yml
│       ├── productos_post.yml
│       ├── productos_put.yml
│       └── productos_delete.yml
├── migrations/
│   ├── versions/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── tests/
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

**Nota:** El archivo `.env` se mantiene únicamente en el entorno local y no debe publicarse en GitHub.

### Responsabilidades

- **main.py:** configura Flask, registra Blueprints, inicializa SQLAlchemy y Flask-Migrate, y define middlewares y manejadores de errores.
- **config.py:** obtiene las variables de entorno y configura la conexión con PostgreSQL.
- **app/extensions.py:** declara las instancias compartidas de SQLAlchemy y Flask-Migrate.
- **routes:** registra los endpoints mediante Flask Blueprints.
- **controllers:** procesa solicitudes HTTP, ejecuta operaciones CRUD y genera respuestas JSON.
- **models:** contiene las clases del dominio y los modelos ORM que representan las tablas de PostgreSQL.
- **services:** conserva el almacenamiento temporal utilizado en las sesiones anteriores como referencia del desarrollo inicial.
- **docs/swagger:** contiene los archivos YAML de documentación de la API.
- **migrations:** registra los cambios de estructura de la base de datos.
- **tests:** contiene ejercicios y pruebas desarrollados durante el curso.

## 6. Validaciones y manejo de errores

La aplicación incorpora validaciones mediante la clase `Producto`, incluyendo la verificación de campos obligatorios y restricciones sobre los datos.

También se verifica que la categoría indicada exista antes de registrar o actualizar un producto.

La API contempla respuestas para situaciones como:

- **200 OK:** consulta, actualización o eliminación exitosa.
- **201 Created:** producto registrado correctamente.
- **400 Bad Request:** datos inválidos, campos obligatorios faltantes o categoría inexistente.
- **404 Not Found:** producto o ruta no encontrada.
- **500 Internal Server Error:** error interno o fallo al procesar una operación.

Se implementaron además los mecanismos `before_request` y `after_request` para registrar solicitudes HTTP y agregar un encabezado personalizado a las respuestas.

Las operaciones de escritura utilizan transacciones de SQLAlchemy. En caso de error durante una operación, se ejecuta `rollback()` para revertir los cambios pendientes.

## 7. Documentación OpenAPI/Swagger

La API utiliza Flasgger para visualizar su documentación interactiva.

Con Flask ejecutándose, acceder desde el navegador a:

http://127.0.0.1:5000/apidocs/

Se documentaron los siguientes endpoints:

- GET `/api/productos`
- POST `/api/productos`
- PUT `/api/productos/{codigo}`
- DELETE `/api/productos/{codigo}`

Cada operación contiene la descripción de su funcionamiento, los parámetros requeridos y las respuestas HTTP correspondientes.

Durante la Sesión 5 se actualizaron los archivos YAML para reflejar el almacenamiento en PostgreSQL.

En las operaciones POST y PUT se utiliza `id_categoria` como referencia a una categoría registrada.

## 8. Persistencia de datos con PostgreSQL

Durante la Sesión 5 se integró una base de datos relacional PostgreSQL para reemplazar el almacenamiento temporal utilizado inicialmente por la API.

### 8.1. Base de datos

Nombre utilizado durante el desarrollo:

`muebletech_ves`

La administración de la base de datos se realiza mediante pgAdmin 4.

Se configuró un usuario de acceso a PostgreSQL con permisos para trabajar sobre la base de datos del proyecto.

### 8.2. Modelo relacional

Se implementaron dos tablas principales:

**Tabla categorias**

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id_categoria | INTEGER | Clave primaria autoincremental |
| nombre | VARCHAR(100) | Nombre único de la categoría |
| descripcion | VARCHAR(255) | Descripción opcional |

**Tabla productos**

| Campo | Tipo de dato | Descripción |
|---|---|---|
| codigo | INTEGER | Clave primaria autoincremental |
| nombre | VARCHAR(150) | Nombre del producto |
| precio | NUMERIC(10,2) | Precio del producto |
| stock | INTEGER | Cantidad disponible |
| id_categoria | INTEGER | Clave foránea hacia categorias |

### 8.3. Relación uno a muchos (1:N)

La relación entre ambas tablas se establece mediante:

`productos.id_categoria → categorias.id_categoria`

Esto significa que:

- Una categoría puede contener varios productos.
- Cada producto pertenece a una categoría.
- La clave foránea garantiza la integridad referencial.

La relación se implementó mediante los modelos ORM `CategoriaDB` y `ProductoDB`, utilizando `db.relationship()` y `db.ForeignKey()`.

### 8.4. Validación de la relación

Se registraron categorías como Mesas, Sillas y Salas.

Posteriormente, se insertaron productos asociados a dichas categorías y se realizaron consultas SQL utilizando `INNER JOIN`.

También se registraron varios productos asociados a la categoría Mesas para demostrar la relación uno a muchos.

## 9. Migraciones con Flask-Migrate

Se incorporó Flask-Migrate para administrar los cambios de estructura de la base de datos.

Durante la configuración inicial se ejecutaron los siguientes comandos:

```powershell
python -m flask --app main:app db init
```

Inicializa el directorio de migraciones.

```powershell
python -m flask --app main:app db migrate -m "Crear tablas categorias y productos relacion 1 a N"
```

Genera una migración a partir de los modelos SQLAlchemy.

```powershell
python -m flask --app main:app db upgrade
```

Aplica las migraciones pendientes en PostgreSQL.

Como resultado, se crearon las tablas `categorias` y `productos`, además de `alembic_version`, utilizada para controlar las versiones de migración.

**Importante:** `db init` se ejecuta únicamente cuando todavía no existe el directorio de migraciones. En una instalación nueva del proyecto que ya incluye `migrations/`, se utiliza `db upgrade` para aplicar las migraciones existentes.

## 10. Configuración del entorno local

### 10.1. Requisitos

Para ejecutar el proyecto se necesita:

- Python compatible con las dependencias del proyecto.
- PostgreSQL.
- Un usuario de PostgreSQL con permisos sobre la base de datos.
- Visual Studio Code u otro editor.
- Git, si se desea clonar el repositorio.

### 10.2. Clonar el proyecto

```powershell
git clone https://github.com/Zoe26/MuebleTech-VES.git
```

Ingresar al directorio:

```powershell
cd MuebleTech-VES
```

### 10.3. Crear el entorno virtual

```powershell
python -m venv .venv
```

Activar el entorno virtual en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 10.4. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 10.5. Preparar PostgreSQL

Crear en PostgreSQL una base de datos denominada:

`muebletech_ves`

También se debe disponer de un usuario con permisos suficientes para conectarse y aplicar las migraciones.

### 10.6. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto y definir los siguientes valores:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=muebletech_ves
DB_USER=usuario_local
DB_PASSWORD=contrasena_local
```

Reemplazar `usuario_local` y `contrasena_local` por las credenciales del entorno de ejecución.

El archivo `.env` está excluido del control de versiones mediante `.gitignore`.

No se deben almacenar contraseñas reales directamente en `config.py`, `README.md` ni en archivos publicados en GitHub.

### 10.7. Aplicar las migraciones

Con PostgreSQL en funcionamiento y las variables de entorno configuradas, ejecutar:

```powershell
python -m flask --app main:app db upgrade
```

Este comando crea o actualiza las tablas conforme a las migraciones existentes.

### 10.8. Iniciar la aplicación

```powershell
python main.py
```

La aplicación estará disponible localmente en:

http://127.0.0.1:5000/

La documentación Swagger estará disponible en:

http://127.0.0.1:5000/apidocs/

## 11. Pruebas del CRUD persistente

Se realizaron pruebas de las operaciones principales utilizando Thunder Client y Swagger.

### 11.1. Consultar productos

**Método:** GET

**Endpoint:** `/api/productos`

Recupera los productos almacenados en PostgreSQL, incluyendo el nombre de la categoría asociada.

### 11.2. Registrar un producto

**Método:** POST

**Endpoint:** `/api/productos`

Ejemplo de solicitud JSON:

```json
{
  "nombre": "Mesa de trabajo industrial",
  "precio": 580.00,
  "stock": 7,
  "id_categoria": 1
}
```

El código del producto es generado automáticamente por PostgreSQL.

La respuesta exitosa utiliza el estado HTTP `201 Created`.

### 11.3. Actualizar un producto

**Método:** PUT

**Endpoint:** `/api/productos/{codigo}`

Ejemplo de solicitud JSON:

```json
{
  "nombre": "Mesa de trabajo industrial premium",
  "precio": 650.00,
  "stock": 10,
  "id_categoria": 1
}
```

La operación modifica el producto identificado por su código.

La respuesta exitosa utiliza el estado HTTP `200 OK`.

### 11.4. Eliminar un producto

**Método:** DELETE

**Endpoint:** `/api/productos/{codigo}`

Elimina el producto identificado por su código.

La respuesta exitosa utiliza el estado HTTP `200 OK`.

Si el producto no existe, la API devuelve `404 Not Found`.

### 11.5. Comprobación de persistencia

Después de realizar las operaciones CRUD, se detuvo y reinició la aplicación Flask.

Posteriormente, se ejecutó nuevamente GET `/api/productos` para verificar que los registros continuaban almacenados en PostgreSQL.

La prueba confirmó que la información permanece disponible después de reiniciar el servidor, a diferencia del almacenamiento temporal utilizado en las sesiones anteriores.

## 12. Seguridad y control de versiones

El proyecto utiliza Git y GitHub para el seguimiento de cambios.

Las credenciales de PostgreSQL se administran mediante variables de entorno.

El archivo `.gitignore` excluye archivos locales y temporales, entre ellos:

- `.env`
- `.env.*`
- `.venv/`
- `__pycache__/`
- `*.pyc`

Se verificó que `.env` está excluido y que Git no lo tiene registrado como archivo rastreado.

Las migraciones de base de datos sí se conservan en el repositorio para facilitar la configuración del proyecto en otros entornos.

La autenticación JWT y las medidas adicionales de protección de endpoints se abordarán en la Sesión 6.

## 13. Avance del proyecto por sesiones

| Sesión | Tema | Estado |
|---|---|---|
| 1 | Configuración del entorno, Python y Git | Desarrollado |
| 2 | Programación orientada a objetos y excepciones | Desarrollado |
| 3 | Fundamentos de Flask, rutas y métodos HTTP | Desarrollado |
| 4 | Arquitectura REST, Blueprints, Controllers y Swagger | Desarrollado |
| 5 | PostgreSQL, SQLAlchemy, Flask-Migrate y CRUD persistente | Implementado y probado |
| 6 | Seguridad, autenticación JWT y variables de entorno | Pendiente |
| 7 | Despliegue en la nube | Pendiente |
| 8 | Presentación y demostración del proyecto final | Pendiente |

## 14. Resultados alcanzados

Hasta la Sesión 5 se ha desarrollado una API REST que permite:

1. Gestionar un catálogo de muebles industriales.
2. Aplicar programación orientada a objetos y validaciones.
3. Organizar el código mediante Blueprints y Controllers.
4. Documentar los endpoints mediante Swagger.
5. Conectarse a una base de datos PostgreSQL.
6. Modelar tablas relacionadas mediante SQLAlchemy.
7. Administrar migraciones con Flask-Migrate.
8. Ejecutar operaciones CRUD persistentes.
9. Recuperar información relacionada entre productos y categorías.
10. Mantener los datos almacenados después de reiniciar Flask.

El proyecto constituye la base para incorporar autenticación, autorización y despliegue en las siguientes sesiones.

## 15. Próximas mejoras

Durante las siguientes etapas del curso se contempla:

- Implementar autenticación mediante JWT.
- Incorporar mecanismos de protección de contraseñas.
- Proteger los endpoints que requieran autenticación.
- Configurar mecanismos adicionales de seguridad.
- Preparar el despliegue de la API.
- Integrar posteriormente la API con una interfaz web para la gestión del catálogo.

## 16. Repositorio

GitHub:

https://github.com/Zoe26/MuebleTech-VES
