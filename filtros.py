# filtros.py
# Módulo de filtrado de países
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Lucas Pianelli
# Correciones: Ezequiel Gómez


def filtrar_continente(paises):
    continentes = set()
    for p in paises:
        continentes.add(p["continente"])

    print("Continentes disponibles:")
    for c in sorted(continentes):
        print(f"  {c}")

    continente = input("Ingresa el continente: ")

    resultado = []
    for p in paises:
        if p["continente"].lower() == continente.lower():
            resultado.append(p)

    if len(resultado) == 0:
        print(f"No se encontraron paises en {continente}.")
    else:
        print(f"Paises en {continente}:")
        for p in resultado:
            print(f"  {p['nombre']}")

    return resultado


def filtrar_poblacion(paises):
    while True:
        try:
            minimo = int(input("Ingresa la población mínima: "))
            maximo = int(input("Ingresa la población máxima: "))

            if minimo > maximo:
                print("Error: la población mínima no puede ser mayor que la máxima.")
            else:
                break

        except ValueError:
            print("Error: ingresa números válidos.")

    resultado = []

    for p in paises:
        poblacion = int(p["poblacion"])

        if minimo <= poblacion <= maximo:
            resultado.append(p)

    if len(resultado) == 0:
        print("No se encontraron países en ese rango de población.")
    else:
        print(f"Países con población entre {minimo} y {maximo}:")
        for p in resultado:
            print(f"  {p['nombre']}: {p['poblacion']} hab.")

    return resultado


def filtrar_superficie(paises):
    while True:
        try:
            minimo = int(input("Ingresa la superficie minima en km2: "))
            break
        except ValueError:
            print("Error: ingresa un numero valido.")

    resultado = []
    for p in paises:
        if int(p["superficie"]) >= minimo:
            resultado.append(p)

    if len(resultado) == 0:
        print("No se encontraron paises con esa superficie minima.")
    else:
        print(f"Paises con superficie mayor o igual a {minimo} km2:")
        for p in resultado:
            print(f"  {p['nombre']}: {p['superficie']} km2")

    return resultado
