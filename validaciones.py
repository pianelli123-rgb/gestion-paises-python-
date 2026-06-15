# Validaciones.py
# Módulo de estadísticas de países
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Ezequiel Gómez

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el campo no puede estar vacío.")
        else:
            return texto


def validar_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: debe ingresar un número mayor que 0.")

        except ValueError:
            print("Error: ingrese un número válido.")


def agregar_pais(paises):
    print("\n=== Agregar país ===")

    nombre = validar_texto("Nombre: ")

    # Verificar que no exista
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    poblacion = validar_entero_positivo("Población: ")
    superficie = validar_entero_positivo("Superficie (km²): ")
    continente = validar_texto("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("País agregado correctamente.")
    return paises

def actualizar_pais(paises):
    print("\n=== Actualizar país ===")

    nombre = validar_texto("Ingrese el nombre del país: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():

            print(f"Actualizando datos de {pais['nombre']}")

            pais["poblacion"] = validar_entero_positivo(
                "Nueva población: "
            )

            pais["superficie"] = validar_entero_positivo(
                "Nueva superficie (km²): "
            )

            print("Datos actualizados correctamente.")
            return paises

    print("No se encontró el país.")
    return paises
