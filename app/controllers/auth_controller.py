
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models.usuario_db import UsuarioDB
from app.services.seguridad_service import generar_hash_password

from flask_jwt_extended import create_access_token
from app.services.seguridad_service import verificar_password
from flasgger import swag_from
from pathlib import Path


@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "auth_registro.yml"
    )
)
def registrar_usuario():

    # 1. Recibir la información enviada como JSON
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    # 2. Verificar los campos obligatorios
    campos = ["nombre", "correo", "password"]

    for campo in campos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    # 3. Validar los datos recibidos
    nombre = datos["nombre"]
    correo = datos["correo"]
    password = datos["password"]

    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({
            "mensaje": "El nombre es obligatorio"
        }), 400

    if len(nombre.strip()) > 100:
        return jsonify({
            "mensaje": "El nombre no debe superar 100 caracteres"
        }), 400

    if not isinstance(correo, str) or not correo.strip():
        return jsonify({
            "mensaje": "El correo es obligatorio"
        }), 400

    correo = correo.strip().lower()

    if (
        len(correo) > 150
        or correo.count("@") != 1
        or "." not in correo.split("@")[1]
    ):
        return jsonify({
            "mensaje": "Ingrese un correo electrónico válido"
        }), 400

    # 4. Impedir que el usuario asigne su propio rol
    if "rol" in datos or "activo" in datos:
        return jsonify({
            "mensaje": "No se permite asignar rol ni estado"
        }), 400

    # 5. Verificar que el correo no esté registrado
    existente = db.session.execute(
        db.select(UsuarioDB).filter_by(correo=correo)
    ).scalar_one_or_none()

    if existente is not None:
        return jsonify({
            "mensaje": "El correo ya está registrado"
        }), 409

    # 6. Generar el hash de la contraseña
    try:
        password_hash = generar_hash_password(password)
    except (ValueError, TypeError) as error:
        return jsonify({
            "mensaje": str(error)
        }), 400

    # 7. Crear el usuario con rol predeterminado
    nuevo_usuario = UsuarioDB(
        nombre=nombre.strip(),
        correo=correo,
        password_hash=password_hash,
        rol="usuario",
        activo=True
    )

    # 8. Guardar en PostgreSQL
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "mensaje": "El correo ya está registrado"
        }), 409

    except Exception:
        db.session.rollback()
        return jsonify({
            "mensaje": "No se pudo registrar el usuario"
        }), 500

    # 9. Responder sin exponer el hash
    return jsonify({
        "mensaje": "Usuario registrado correctamente",
        "usuario": {
            "id_usuario": nuevo_usuario.id_usuario,
            "nombre": nuevo_usuario.nombre,
            "correo": nuevo_usuario.correo,
            "rol": nuevo_usuario.rol
        }
    }), 201


@swag_from(
    str(
        Path(__file__).resolve().parents[2]
        / "docs" / "swagger" / "auth_login.yml"
    )
)
def iniciar_sesion():

    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "mensaje": "Debe enviar un objeto JSON válido"
        }), 400

    correo = datos.get("correo")
    password = datos.get("password")

    if (
        not isinstance(correo, str)
        or not correo.strip()
        or not isinstance(password, str)
        or not password
    ):
        return jsonify({
            "mensaje": "Correo y contraseña son obligatorios"
        }), 400

    correo = correo.strip().lower()

    usuario = db.session.execute(
        db.select(UsuarioDB).filter_by(correo=correo)
    ).scalar_one_or_none()

    if usuario is None or not verificar_password(
        password, usuario.password_hash
    ):
        return jsonify({
            "mensaje": "Credenciales incorrectas"
        }), 401

    if not usuario.activo:
        return jsonify({
            "mensaje": "Cuenta deshabilitada"
        }), 403

    access_token = create_access_token(
        identity=str(usuario.id_usuario)
    )

    return jsonify({
        "mensaje": "Inicio de sesión exitoso",
        "access_token": access_token,
        "token_type": "Bearer",
        "usuario": {
            "id_usuario": usuario.id_usuario,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "rol": usuario.rol
        }
    }), 200
