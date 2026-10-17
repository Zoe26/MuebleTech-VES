
# MuebleTech VES
# Sesión 2: Excepciones personalizadas


class PrecioInvalidoError(ValueError):
    """Error cuando el precio de un producto es inválido."""
    pass


class StockInvalidoError(ValueError):
    """Error cuando el stock de un producto es inválido."""
    pass


class ProductoNoEncontradoError(Exception):
    """Error cuando no se encuentra un producto."""
    pass
