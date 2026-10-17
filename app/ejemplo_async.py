
# MuebleTech VES
# Sesión 1: Introducción a async/await

import asyncio


async def consultar_producto(nombre):
    print(f"Iniciando consulta: {nombre}")

    # Simulamos una espera de dos segundos.
    await asyncio.sleep(2)

    print(f"Consulta finalizada: {nombre}")


async def main():
    await asyncio.gather(
        consultar_producto("Mesa industrial"),
        consultar_producto("Estantería metálica")
    )


if __name__ == "__main__":
    asyncio.run(main())
