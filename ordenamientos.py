# ordenamientos.py
# Módulo de ordenamiento de países
# TPI Programación 1 - UTN TUPAD 168 2026
# Autor: Lucas Pianelli


def obtener_nombre(p):
    return p["nombre"].lower()

def obtener_poblacion(p):
    return int(p["poblacion"])

def obtener_superficie(p):
    return int(p["superficie"])


def ordenar_nombre(paises):
    resultado = sorted(paises, key=obtener_nombre)
    print("Paises ordenados por nombre:")
    for p in resultado:
        print(f"  {p['nombre']}")
    return resultado


def ordenar_poblacion(paises):
    resultado = sorted(paises, key=obtener_poblacion, reverse=True)
    print("Paises ordenados por poblacion (mayor a menor):")
    for p in resultado:
        print(f"  {p['nombre']}: {p['poblacion']} hab.")
    return resultado


def ordenar_superficie(paises):
    resultado = sorted(paises, key=obtener_superficie, reverse=True)
    print("Paises ordenados por superficie (mayor a menor):")
    for p in resultado:
        print(f"  {p['nombre']}: {p['superficie']} km2")
    return resultado
