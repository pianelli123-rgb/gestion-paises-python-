# main.py
# Punto de entrada y menú principal
# TPI Programación 1 - UTN TUPAD 168 2026
# Autores: Lucas Pianelli, EZEQUIEL GOMEZ

from datos import cargar_paises, guardar_paises, mostrar_paises
from validaciones import agregar_pais, actualizar_pais
from filtros import filtrar_continente, filtrar_poblacion, filtrar_superficie
from ordenamientos import ordenar_nombre, ordenar_poblacion, ordenar_superficie
from estadisticas import estadisticas


def mostrar_menu():
    print("\n=== Gestión de Datos de Países ===")
    print("1. Mostrar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar un país")
    print("4. Filtrar por continente")
    print("5. Filtrar por población mínima")
    print("6. Filtrar por superficie mínima")
    print("7. Ordenar por nombre")
    print("8. Ordenar por población")
    print("9. Ordenar por superficie")
    print("10. Ver estadísticas")
    print("0. Salir")


def main():
    paises = cargar_paises()

    while True:
        mostrar_menu()

        opcion = input("\nElegí una opción: ").strip()

        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            paises = agregar_pais(paises)
            guardar_paises(paises)
        elif opcion == "3":
            paises = actualizar_pais(paises)
            guardar_paises(paises)
        elif opcion == "4":
            filtrar_continente(paises)
        elif opcion == "5":
            filtrar_poblacion(paises)
        elif opcion == "6":
            filtrar_superficie(paises)
        elif opcion == "7":
            ordenar_nombre(paises)
        elif opcion == "8":
            ordenar_poblacion(paises)
        elif opcion == "9":
            ordenar_superficie(paises)
        elif opcion == "10":
            estadisticas(paises)
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Ingresá un número del 0 al 10.")


main()
