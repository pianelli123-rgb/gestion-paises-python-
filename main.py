# main.py
# Punto de entrada y menú principal
# TPI Programación 1 - UTN TUPAD 168 2026
# Autores: Lucas Pianelli, Ezequiel Gomez

from datos import cargar_paises, guardar_paises, mostrar_paises
from validaciones import agregar_pais, actualizar_pais
from filtros import filtrar_continente, filtrar_poblacion, filtrar_superficie
from ordenamientos import ordenar_nombre, ordenar_poblacion, ordenar_superficie,buscar_pais
from estadisticas import estadisticas



def mostrar_menu():
    print("Gestion de Datos de Paises")
    print("1. Mostrar todos los paises")
    print("2. Agregar un pais")
    print("3. Actualizar un pais")
    print("4. Filtrar por continente")
    print("5. Buscar Pais")
    print("6. Filtrar por rango de población")
    print("7. Filtrar por rango de superficie")
    print("8. Ordenar por nombre")
    print("9. Ordenar por poblacion")
    print("10. Ordenar por superficie")
    print("11. Ver estadisticas")
    print("0. Salir")


def main():
    paises = cargar_paises()

    while True:
        mostrar_menu()
        opcion = input("Elegi una opcion: ").strip()

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
            buscar_pais(paises)
        elif opcion == "6":
            filtrar_poblacion(paises)
        elif opcion == "7":
            filtrar_superficie(paises)
        elif opcion == "8":
            ordenar_nombre(paises)
        elif opcion == "9":
            ordenar_poblacion(paises)
        elif opcion == "10":
            ordenar_superficie(paises)
        elif opcion == "11":
            estadisticas(paises)
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Ingresa un numero del 0 al 10.")


main()
