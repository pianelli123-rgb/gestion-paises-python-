# filtros.py
# Módulo de filtrado de países
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Lucas Pianelli


def filtrar_continente(paises):
    """Filtra y muestra los países de un continente ingresado por el usuario."""
    continentes_disponibles = sorted(set(p["continente"] for p in paises))

    print("\n--- Filtrar por Continente ---")
    print("Continentes disponibles:")
    for c in continentes_disponibles:
        print(f"  - {c}")

    continente = input("\nIngresá el continente: ").strip().capitalize()

    resultado = [p for p in paises if p["continente"].lower() == continente.lower()]

    if resultado:
        print(f"\nPaíses en {continente} ({len(resultado)} encontrados):")
        print(f"{'Nombre':<20} {'Población':>15} {'Superficie (km²)':>18}")
        print("-" * 55)
        for p in resultado:
            print(f"{p['nombre']:<20} {int(p['poblacion']):>15,} {int(p['superficie']):>18,}")
    else:
        print(f"\nNo se encontraron países en el continente '{continente}'.")

    return resultado


def filtrar_poblacion(paises):
    """Filtra y muestra los países con población mayor a un valor ingresado."""
    print("\n--- Filtrar por Población Mínima ---")

    while True:
        try:
            minimo = int(input("Ingresá la población mínima: ").strip())
            break
        except ValueError:
            print("Error: ingresá un número entero válido.")

    resultado = [p for p in paises if int(p["poblacion"]) >= minimo]

    if resultado:
        print(f"\nPaíses con población >= {minimo:,} ({len(resultado)} encontrados):")
        print(f"{'Nombre':<20} {'Población':>15} {'Continente':>12}")
        print("-" * 50)
        for p in sorted(resultado, key=lambda x: int(x["poblacion"]), reverse=True):
            print(f"{p['nombre']:<20} {int(p['poblacion']):>15,} {p['continente']:>12}")
    else:
        print(f"\nNo se encontraron países con población mayor a {minimo:,}.")

    return resultado


def filtrar_superficie(paises):
    """Filtra y muestra los países con superficie mayor a un valor ingresado."""
    print("\n--- Filtrar por Superficie Mínima ---")

    while True:
        try:
            minimo = int(input("Ingresá la superficie mínima (km²): ").strip())
            break
        except ValueError:
            print("Error: ingresá un número entero válido.")

    resultado = [p for p in paises if int(p["superficie"]) >= minimo]

    if resultado:
        print(f"\nPaíses con superficie >= {minimo:,} km² ({len(resultado)} encontrados):")
        print(f"{'Nombre':<20} {'Superficie (km²)':>18} {'Continente':>12}")
        print("-" * 52)
        for p in sorted(resultado, key=lambda x: int(x["superficie"]), reverse=True):
            print(f"{p['nombre']:<20} {int(p['superficie']):>18,} {p['continente']:>12}")
    else:
        print(f"\nNo se encontraron países con superficie mayor a {minimo:,} km².")

    return resultado
