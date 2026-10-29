
from app.extensions import bcrypt


def generar_hash_password(password):
    """
    Genera un hash seguro de la contraseña
    utilizando bcrypt.
    """

    if not isinstance(password, str):
        raise ValueError("La contraseña debe ser texto")

    if len(password) < 12:
        raise ValueError(
            "La contraseña debe tener al menos 12 caracteres"
        )

    if len(password.encode("utf-8")) > 72:
        raise ValueError(
            "La contraseña supera el límite admitido"
        )

    password_hash = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    return password_hash


def verificar_password(password, password_hash):
    """
    Comprueba si la contraseña ingresada
    corresponde al hash almacenado.
    """

    if not isinstance(password, str):
        return False

    if not isinstance(password_hash, str):
        return False

    return bcrypt.check_password_hash(
        password_hash,
        password
    )
