# filtros.py
# Módulo de filtrado de países
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Lucas Pianelli


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
            minimo = int(input("Ingresa la poblacion minima: "))
            break
        except ValueError:
            print("Error: ingresa un numero valido.")

    resultado = []
    for p in paises:
        if int(p["poblacion"]) >= minimo:
            resultado.append(p)

    if len(resultado) == 0:
        print("No se encontraron paises con esa poblacion minima.")
    else:
        print(f"Paises con poblacion mayor o igual a {minimo}:")
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
