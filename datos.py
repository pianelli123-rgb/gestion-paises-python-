# datos.py
# Módulo de carga y gestión de datos
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Ezequiel Gómez


def cargar_paises():
    paises = []
    try:
        archivo = open("data/paises.csv", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea != "":
                partes = linea.split(",")
                pais = {
                    "nombre": partes[0],
                    "poblacion": partes[1],
                    "superficie": partes[2],
                    "continente": partes[3]
                }
                paises.append(pais)

        print(f"Se cargaron {len(paises)} países correctamente.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo paises.csv.")

    return paises


def guardar_paises(paises):
    try:
        archivo = open("data/paises.csv", "w", encoding="utf-8")
        archivo.write("nombre,poblacion,superficie,continente\n")
        for p in paises:
            linea = f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
            archivo.write(linea)
        archivo.close()
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")


def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    print(f"\nTotal de países: {len(paises)}")
    for p in paises:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")
