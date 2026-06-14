# estadisticas.py
# Módulo de estadísticas de países
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Lucas Pianelli


def obtener_poblacion(p):
    return int(p["poblacion"])

def obtener_superficie(p):
    return int(p["superficie"])


def estadisticas(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    total_poblacion = sum(int(p["poblacion"]) for p in paises)
    total_superficie = sum(int(p["superficie"]) for p in paises)
    promedio_poblacion = total_poblacion // len(paises)
    promedio_superficie = total_superficie // len(paises)

    mas_poblado = max(paises, key=obtener_poblacion)
    menos_poblado = min(paises, key=obtener_poblacion)
    mas_grande = max(paises, key=obtener_superficie)
    mas_chico = min(paises, key=obtener_superficie)

    continentes = {}
    for p in paises:
        c = p["continente"]
        if c in continentes:
            continentes[c] += 1
        else:
            continentes[c] = 1

    print("Estadisticas generales")
    print(f"Total de paises: {len(paises)}")
    print(f"Poblacion total: {total_poblacion}")
    print(f"Superficie total: {total_superficie} km2")
    print(f"Poblacion promedio: {promedio_poblacion} hab.")
    print(f"Superficie promedio: {promedio_superficie} km2")
    print(f"Pais mas poblado: {mas_poblado['nombre']} ({mas_poblado['poblacion']} hab.)")
    print(f"Pais menos poblado: {menos_poblado['nombre']} ({menos_poblado['poblacion']} hab.)")
    print(f"Pais mas grande: {mas_grande['nombre']} ({mas_grande['superficie']} km2)")
    print(f"Pais mas pequeño: {mas_chico['nombre']} ({mas_chico['superficie']} km2)")
    print("Paises por continente:")
    for c in sorted(continentes):
        print(f"  {c}: {continentes[c]}")
