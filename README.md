# MuebleTech VES

> **Actualización de entrega (sesiones 7 y 8):** Se conservan íntegramente las secciones históricas 1 a 17 que documentan la evolución del proyecto. Algunas frases de esas secciones describen estados anteriores (por ejemplo, despliegue pendiente y rol `admin` como único permiso de escritura). Las **secciones 18 a 22** presentan el estado actualizado y prevalecen cuando hay diferencias. El frontend no forma parte del alcance de la entrega.

## 1. Descripción del proyecto
****MuebleTech VES**** es un proyecto de desarrollo Back End orientado a la gestión de un catálogo de muebles industriales del Parque Industrial de Villa El Salvador, Lima, Perú.

El sistema permite registrar, consultar, actualizar y eliminar productos mediante una ****API REST desarrollada con Python y Flask****, aplicando programación orientada a objetos, validaciones de datos, manejo de errores HTTP y una arquitectura modular basada en Blueprints y Controllers.

A partir de la Sesión 5, la aplicación incorpora ****persistencia de datos con PostgreSQL y Flask-SQLAlchemy****, permitiendo almacenar permanentemente los productos y relacionarlos con sus respectivas categorías.

El proyecto se desarrolla progresivamente como parte del curso de Programación Back End, incorporando nuevas funcionalidades durante ocho sesiones.

## 2. Objetivo general
Desarrollar una API REST que permita gestionar muebles industriales mediante operaciones CRUD, utilizando Python y Flask, con arquitectura modular, documentación OpenAPI/Swagger, persistencia en PostgreSQL mediante Flask-SQLAlchemy y protección de operaciones administrativas a través de autenticación JWT y autorización por roles.

La API incluye autenticación JWT, contraseñas protegidas mediante bcrypt y autorización por roles. El despliegue en la nube y la integración final del frontend se abordarán en las siguientes sesiones.

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

| Flask-JWT-Extended | Autenticación mediante tokens JWT | Implementado |

| Flask-Bcrypt | Hashing y verificación de contraseñas | Implementado |

| Flask-Cors | Configuración de orígenes permitidos | Implementado |

| Flask-Limiter | Límite de solicitudes de inicio de sesión | Implementado |

## 4. Funcionalidades implementadas
La API permite realizar las siguientes operaciones:

| Método HTTP | Endpoint | Descripción |

|---|---|---|

| GET | `/api/productos` | Consultar todos los productos almacenados en PostgreSQL |

| POST | `/api/productos` | Registrar un nuevo producto |

| PUT | `/api/productos/{codigo}` | Actualizar un producto existente |

| DELETE | `/api/productos/{codigo}` | Eliminar un producto |

| GET | `/api/productos/prueba` | Verificar el funcionamiento del Blueprint |

La API devuelve respuestas JSON y utiliza códigos HTTP 200, 201, 400, 401, 403, 404, 409, 429 y 500. Los endpoints GET del catálogo son públicos; POST, PUT y DELETE de productos requieren JWT válido y rol `admin`.

Las operaciones CRUD principales utilizan Flask-SQLAlchemy para interactuar con PostgreSQL, garantizando que los cambios se mantengan almacenados después de reiniciar la aplicación.

## 5. Arquitectura del proyecto
MuebleTech VES utiliza una organización modular que separa las responsabilidades de la aplicación.

```text

MuebleTech-VES/

├── .vscode/

│   └── launch.json

├── app/

│   ├── controllers/

│   │   ├── \_\_init\_\_.py

│   │   └── productos_controller.py

│   ├── models/

│   │   ├── producto.py

│   │   ├── mueble_industrial.py

│   │   ├── categoria.py

│   │   ├── usuario.py

│   │   ├── categoria_db.py

│   │   └── producto_db.py

│   ├── routes/

│   │   └── productos_routes.py

│   ├── services/

│   │   └── productos_data.py

│   ├── extensions.py

│   ├── excepciones.py

│   └── \_\_init\_\_.py

├── docs/

│   └── swagger/

│       ├── productos_get.yml

│       ├── productos_post.yml

│       ├── productos_put.yml

│       └── productos_delete.yml

├── migrations/

│   ├── versions/

│   ├── alembic.ini

│   ├── env.py

│   ├── README

│   └── script.py.mako

├── tests/

├── config.py

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

└── .env

```

****Nota:**** El archivo `.env` se mantiene únicamente en el entorno local y no debe publicarse en GitHub.

### Responsabilidades
\- ****main.py:**** configura Flask, SQLAlchemy, Flask-Migrate, bcrypt, JWT, CORS y Flask-Limiter, registra Blueprints, Swagger, middlewares y manejadores de errores.

\- ****config.py:**** lee las variables de entorno y configura PostgreSQL, la clave/expiración JWT y los orígenes CORS.

\- ****app/extensions.py:**** declara las extensiones compartidas de SQLAlchemy, Migrate, Bcrypt, JWTManager, CORS y Limiter.

\- ****routes:**** registra los endpoints mediante Flask Blueprints.

\- ****controllers:**** procesa solicitudes HTTP, ejecuta operaciones CRUD y genera respuestas JSON.

\- ****models:**** contiene las clases del dominio y los modelos ORM que representan las tablas de PostgreSQL.

\- ****services:**** conserva la referencia de almacenamiento temporal de sesiones anteriores e incluye hashing de contraseñas y autorización de administradores.

\- ****docs/swagger:**** contiene los archivos YAML de documentación de la API.

\- ****migrations:**** registra los cambios de estructura de la base de datos.

\- ****tests:**** contiene ejercicios y pruebas desarrollados durante el curso.

## 6. Validaciones y manejo de errores
La aplicación incorpora validaciones mediante la clase `Producto`, incluyendo la verificación de campos obligatorios y restricciones sobre los datos.

También se verifica que la categoría indicada exista antes de registrar o actualizar un producto.

La API contempla respuestas para situaciones como:

\- ****200 OK:**** consulta, actualización o eliminación exitosa.

\- ****201 Created:**** producto registrado correctamente.

\- ****400 Bad Request:**** datos inválidos, campos obligatorios faltantes o categoría inexistente.

\- ****404 Not Found:**** producto o ruta no encontrada.

\- ****401 Unauthorized:**** falta un token válido o las credenciales son incorrectas.

\- ****403 Forbidden:**** el usuario autenticado carece de permisos.

\- ****409 Conflict:**** correo de registro duplicado.

\- ****429 Too Many Requests:**** se superó el límite de solicitudes al login.

\- ****500 Internal Server Error:**** error interno o fallo al procesar una operación.

Se implementaron además los mecanismos `before_request` y `after_request` para registrar solicitudes HTTP y agregar un encabezado personalizado a las respuestas.

Las operaciones de escritura utilizan transacciones de SQLAlchemy. En caso de error durante una operación, se ejecuta `rollback()` para revertir los cambios pendientes.

## 7. Documentación OpenAPI/Swagger
La API utiliza Flasgger para visualizar su documentación interactiva.

Con Flask ejecutándose, acceder desde el navegador a:

http://127.0.0.1:5000/apidocs/

Se documentaron los siguientes endpoints:

\- GET `/api/productos`

\- POST `/api/productos`

\- PUT `/api/productos/{codigo}`

\- DELETE `/api/productos/{codigo}`

\- POST `/api/auth/registro`

\- POST `/api/auth/login`

Cada operación contiene la descripción de su funcionamiento, los parámetros requeridos y las respuestas HTTP correspondientes.

Durante la Sesión 5 se actualizaron los archivos YAML para reflejar el almacenamiento en PostgreSQL.

En las operaciones POST y PUT se utiliza `id_categoria` como referencia a una categoría registrada. Swagger define autenticación `Bearer` para POST, PUT y DELETE de productos; las rutas de autenticación y GET siguen siendo públicas.

## 8. Persistencia de datos con PostgreSQL
Durante la Sesión 5 se integró una base de datos relacional PostgreSQL para reemplazar el almacenamiento temporal utilizado inicialmente por la API.

### 8.1. Base de datos
Nombre utilizado durante el desarrollo:

`muebletech_ves`

La administración de la base de datos se realiza mediante pgAdmin 4.

Se configuró un usuario de acceso a PostgreSQL con permisos para trabajar sobre la base de datos del proyecto.

### 8.2. Modelo relacional
Se implementaron dos tablas principales:

****Tabla categorias****

| Campo | Tipo de dato | Descripción |

|---|---|---|

| id_categoria | INTEGER | Clave primaria autoincremental |

| nombre | VARCHAR(100) | Nombre único de la categoría |

| descripcion | VARCHAR(255) | Descripción opcional |

****Tabla productos****

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

\- Una categoría puede contener varios productos.

\- Cada producto pertenece a una categoría.

\- La clave foránea garantiza la integridad referencial.

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

Como resultado, se crearon las tablas `categorias` y `productos`, además de `alembic_version`, utilizada para controlar las versiones de migración. En la Sesión 6 se creó y aplicó otra migración para incorporar la tabla `usuarios`.

****Importante:**** `db init` se ejecuta únicamente cuando todavía no existe el directorio de migraciones. En una instalación nueva del proyecto que ya incluye `migrations/`, se utiliza `db upgrade` para aplicar las migraciones existentes.

## 10. Configuración del entorno local
### 10.1. Requisitos
Para ejecutar el proyecto se necesita:

\- Python compatible con las dependencias del proyecto.

\- PostgreSQL.

\- Un usuario de PostgreSQL con permisos sobre la base de datos.

\- Visual Studio Code u otro editor.

\- Git, si se desea clonar el repositorio.

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

Activar el entorno virtual en PowerShell (si la política del equipo permite ejecutar scripts):

```powershell

.\\\.venv\Scripts\Activate.ps1

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

JWT_SECRET_KEY=colocar_un_secreto_aleatorio_seguro

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
****Método:**** GET

****Endpoint:**** `/api/productos`

Recupera los productos almacenados en PostgreSQL, incluyendo el nombre de la categoría asociada.

### 11.2. Registrar un producto
****Método:**** POST

****Endpoint:**** `/api/productos`

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
****Método:**** PUT

****Endpoint:**** `/api/productos/{codigo}`

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
****Método:**** DELETE

****Endpoint:**** `/api/productos/{codigo}`

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

\- `.env`

\- `.env.*`

\- `.venv/`

\- `\_\_pycache\_\_/`

\- `*.pyc`

Se verificó que `.env` está excluido y que Git no lo tiene registrado como archivo rastreado.

Las migraciones de base de datos sí se conservan en el repositorio para facilitar la configuración del proyecto en otros entornos.

La Sesión 6 añadió autenticación JWT, hashes bcrypt, permisos por rol, CORS y limitación de intentos de login. En desarrollo local se utiliza `debug=True`; para producción debe desactivarse y configurarse HTTPS y un backend compartido para Flask-Limiter.

## 13. Avance del proyecto por sesiones
| Sesión | Tema | Estado |

|---|---|---|

| 1 | Configuración del entorno, Python y Git | Desarrollado |

| 2 | Programación orientada a objetos y excepciones | Desarrollado |

| 3 | Fundamentos de Flask, rutas y métodos HTTP | Desarrollado |

| 4 | Arquitectura REST, Blueprints, Controllers y Swagger | Desarrollado |

| 5 | PostgreSQL, SQLAlchemy, Flask-Migrate y CRUD persistente | Implementado y probado |

| 6 | Registro seguro, JWT, roles, CORS, Flask-Limiter y Swagger | Implementado y probado localmente |

| 7 | Despliegue en la nube | Pendiente |

| 8 | Presentación y demostración del proyecto final | Pendiente |

## 14. Resultados alcanzados
Hasta la Sesión 6 se ha desarrollado una API REST que permite:

1\. Gestionar un catálogo de muebles industriales.

2\. Aplicar programación orientada a objetos y validaciones.

3\. Organizar el código mediante Blueprints y Controllers.

4\. Documentar los endpoints mediante Swagger.

5\. Conectarse a una base de datos PostgreSQL.

6\. Modelar tablas relacionadas mediante SQLAlchemy.

7\. Administrar migraciones con Flask-Migrate.

8\. Ejecutar operaciones CRUD persistentes.

9\. Recuperar información relacionada entre productos y categorías.

10\. Mantener los datos almacenados después de reiniciar Flask.

La autenticación y autorización están implementadas y verificadas en el entorno local. Las siguientes sesiones abordarán el despliegue y la integración final con el frontend.

## 15. Próximas mejoras
Durante las siguientes etapas del curso se contempla:

\- Mejorar la gestión de secretos y endurecer la configuración para producción.

\- Configurar almacenamiento compartido para el limitador de solicitudes.

\- Preparar el despliegue de la API.

\- Integrar posteriormente la API con una interfaz web para la gestión del catálogo.

## 16. Repositorio
GitHub:

https://github.com/Zoe26/MuebleTech-VES

## 17. Sesión 6: Autenticación, autorización y seguridad
### 17.1. Objetivo
Implementar registro e inicio de sesión de usuarios, hashing de contraseñas, emisión de JWT, control de acceso por roles y buenas prácticas de seguridad sobre el CRUD persistente de MuebleTech VES.

### 17.2. Tabla de usuarios
Se incorporó la tabla `usuarios` mediante una migración con Flask-Migrate. El modelo `UsuarioDB` incluye `id_usuario`, `nombre`, `correo` único, `password_hash`, `rol`, `activo` y `fecha_registro`. Las tablas `categorias` y `productos` permanecen operativas.

### 17.3. Registro y contraseñas protegidas
`POST /api/auth/registro` valida nombre, correo y contraseña; genera un hash bcrypt y guarda únicamente ese hash en PostgreSQL. La API no devuelve el hash. El rol inicial es `usuario` y el registro rechaza que el cliente envíe `rol` o `activo`.

### 17.4. Login y JWT
`POST /api/auth/login` verifica correo y contraseña contra el hash bcrypt y genera un token JWT de acceso. La duración del token se configuró en 30 minutos. La firma depende de `JWT_SECRET_KEY` obtenida de `.env`, nunca de una clave incrustada en el código.

### 17.5. Autorización por roles
`GET /api/productos` es público. `POST`, `PUT` y `DELETE /api/productos` requieren JWT válido y rol `admin`. El decorador `admin_required` consulta el usuario en PostgreSQL para verificar su existencia, estado y rol actual. Las cuentas nuevas se registran como `usuario`; los cambios de rol se administraron manualmente desde PostgreSQL durante las pruebas locales.

### 17.6. CORS y limitación de solicitudes
Se configuró `Flask-Cors` para los orígenes locales `http://localhost:5500` y `http://127.0.0.1:5500`. Se comprobó el encabezado `Access-Control-Allow-Origin` para el origen autorizado. CORS es una política de navegador y no reemplaza JWT.

`Flask-Limiter` restringe el login a `5 per minute` por IP. Al superar el umbral, devuelve HTTP 429 con una respuesta JSON personalizada. El almacenamiento de contadores en memoria se utiliza solo para las pruebas locales.

### 17.7. Resultados de las pruebas manuales
| Prueba | Resultado observado |

|---|---|

| Inicio de sesión válido | 200 OK y JWT |

| Solicitud POST de productos sin JWT | 401 Unauthorized |

| Solicitud POST con JWT de rol `usuario` | 403 Forbidden |

| POST de productos con JWT `admin` | Producto creado y visible en GET |

| PUT de producto con JWT `admin` | 200 OK |

| DELETE de producto con JWT `admin` | 200 OK |

| Origen CORS permitido | Encabezado de origen autorizado comprobado |

| Más de cinco solicitudes de login por minuto | 429 Too Many Requests |

| Respuesta al exceso de solicitudes | JSON con `codigo: 429` |

| Registro que intenta enviar `rol: admin` | 400 Bad Request |

Estas comprobaciones son evidencias funcionales del entorno de desarrollo; no constituyen una auditoría exhaustiva ni una certificación de cumplimiento OWASP API Security Top 10.

### 17.8. Documentación de autenticación
Swagger incorpora `POST /api/auth/registro`, `POST /api/auth/login` y un esquema `Bearer` en el encabezado `Authorization` para las operaciones protegidas del catálogo.

### 17.9. Consideraciones antes de producción
\- Desactivar el modo `debug` de Flask y evitar usar el servidor de desarrollo en producción.

\- Usar HTTPS, políticas de gestión y rotación de secretos y un secreto JWT robusto.

\- Configurar un almacenamiento centralizado o compartido, como Redis, para Flask-Limiter.

\- Revisar autorización, revocación de tokens, gestión de sesiones, cabeceras de seguridad y registro de auditoría antes del despliegue.

\- Ajustar CORS al origen real del frontend desplegado.

****Estado:**** funcionalidades implementadas y comprobadas localmente.


## 18. Sesión 7: despliegue en la nube con Render

Se publicó la API Flask de **MuebleTech VES** en un servicio web gratuito de Render, conectada a una base de datos PostgreSQL administrada por Render. Se utiliza Gunicorn como servidor de aplicación y `render.yaml` para describir el despliegue. La conexión se configura con `DATABASE_URL` mediante variables de entorno, sin publicar credenciales. Flask-Migrate/Alembic aplica las migraciones antes de iniciar Gunicorn.

- **Repositorio público:** https://github.com/Zoe26/MuebleTech-VES
- **API pública:** https://muebletech-ves-api.onrender.com/
- **Productos (GET):** https://muebletech-ves-api.onrender.com/api/productos
- **Categorías (GET):** https://muebletech-ves-api.onrender.com/api/categorias
- **Swagger/OpenAPI:** https://muebletech-ves-api.onrender.com/apidocs/

**Evidencia observada:** Render indicó `Deploy live` para el commit con la adaptación de categorías y roles; la ruta principal respondió correctamente y `GET /api/categorias` devolvió `200 OK` con la lista vacía (`total: 0`), lo cual es válido para la base remota. La documentación Swagger de autenticación, productos y categorías también quedó visible en producción.

**Limitación:** La base de datos local y la base remota son independientes. El plan PostgreSQL gratuito de Render tiene una fecha de vencimiento anunciada en el panel; deben respaldarse los datos antes de que venza. El servicio web gratuito puede entrar en reposo.

## 19. Sesión 8: integración final del Back End

La integración final se enfoca en **API REST + PostgreSQL + JWT + Swagger + Render**. No incluye la interfaz web, que es una mejora opcional y no un requisito del trabajo solicitado.

### 19.1. Operaciones disponibles

| Método | Ruta | Acceso configurado |
|---|---|---|
| GET | `/api/productos` | Público |
| GET | `/api/productos?categoria=1` | Público; filtro por `id_categoria` |
| POST | `/api/productos` | EDITOR o ADMIN |
| PUT | `/api/productos/{codigo}` | EDITOR o ADMIN |
| DELETE | `/api/productos/{codigo}` | ADMIN |
| GET | `/api/categorias` | Público |
| POST | `/api/categorias` | EDITOR o ADMIN |
| PUT | `/api/categorias/{id_categoria}` | EDITOR o ADMIN |
| DELETE | `/api/categorias/{id_categoria}` | ADMIN; rechaza categorías con productos asociados |
| POST | `/api/auth/register` | Público; registra CONSULTA |
| POST | `/api/auth/registro` | Público; alias de compatibilidad |
| POST | `/api/auth/login` | Público; devuelve JWT Bearer |

El registro público rechaza la asignación directa de `rol` y `activo`. Las contraseñas se almacenan como hashes bcrypt y los tokens JWT tienen expiración configurada en `config.py` (30 minutos). La autorización consulta el rol del usuario autenticado en PostgreSQL.

### 19.2. Roles

| Rol | Consultar | Crear | Actualizar | Eliminar |
|---|---|---|---|---|
| CONSULTA | Sí | No | No | No |
| EDITOR | Sí | Sí | Sí | No |
| ADMIN | Sí | Sí | Sí | Sí |

Los usuarios anteriores con rol `usuario` se interpretan como CONSULTA y los antiguos `admin` como ADMIN mediante el servicio de autorización. Los permisos adicionales se administraron manualmente en PostgreSQL durante las pruebas; el registro público no permite elevar privilegios.

## 20. Evidencias funcionales verificadas

Estas pruebas se realizaron **localmente**, salvo las expresamente señaladas como remotas:

| Prueba | Respuesta observada |
|---|---|
| GET `/api/categorias` con categorías locales | `200 OK` y registros devueltos |
| GET `/api/productos?categoria=1` | Filtro funcional |
| Registro de usuario por `/api/auth/register` | `201 Created` |
| Inicio de sesión de EDITOR | `200 OK`, JWT |
| EDITOR registra producto | `201 Created` |
| EDITOR intenta eliminar producto | `403 Forbidden` |
| ADMIN elimina un producto de prueba | `200 OK` |
| CONSULTA inicia sesión | `200 OK`, JWT |
| CONSULTA intenta registrar producto | `403 Forbidden` |
| Render: ruta principal y GET categorías | Respuestas correctas en producción |
| Render: Swagger | Secciones Autenticación, Categorías y Productos visibles |

**No se han confirmado todavía mediante capturas de prueba:** POST, PUT y DELETE de categorías usando los tres roles; respuesta `401` ante token vencido; conjunto completo de validaciones de precio y stock en la versión final; ni operaciones de escritura autenticadas sobre la URL pública de Render.

## 21. Evidencias gráficas para adjuntar

El docente solicita **capturas de pantalla y evidencias de la ejecución**. Al incorporar imágenes al repositorio, se recomienda guardarlas en `docs/evidencias/` y enlazarlas con sintaxis Markdown `![Descripción](docs/evidencias/archivo.png)`. No se incluyen aquí enlaces a archivos que todavía no se han añadido al repositorio.

Capturas sugeridas: estructura del proyecto en VS Code; relación PostgreSQL entre categorías y productos; migraciones; Swagger local o en Render mostrando todos los endpoints; Thunder Client con POST de producto por EDITOR (`201`), intento DELETE por EDITOR (`403`), DELETE por ADMIN (`200`) y POST por CONSULTA (`403`); panel Render `Deploy live`; GET de categorías remotas (`200`). **Ocultar JWT, contraseñas, cadenas de conexión y datos sensibles antes de guardar capturas.**

## 22. Observaciones pendientes y entrega

- **App Factory:** el documento del docente solicita `app/__init__.py` con `create_app()`. La aplicación vigente instancia Flask en `main.py`; una refactorización debe probarse antes de presentarse como cumplida.
- **Errores JSON:** el docente exige formato `{"error": "mensaje seguro"}` en los manejadores globales. Parte del proyecto conserva respuestas con `mensaje`; requiere unificación y prueba de errores `404`, `500` y autenticación.
- **Validaciones:** confirmar con pruebas negativas que precio sea mayor que cero y stock sea entero no negativo.
- **Pruebas de categorías:** verificar POST/PUT/DELETE y la restricción por rol sin eliminar datos de trabajo.
- **Pruebas públicas:** confirmar registro y login por URL pública y guardar capturas sin credenciales.
- **Documentación de entrega:** agregar capturas reales a `docs/evidencias/` y confirmar que el repositorio permanezca público.

**Este README conserva el historial técnico del proyecto y registra el estado de las ocho sesiones sin presentar como verificado lo que continúa pendiente.**
