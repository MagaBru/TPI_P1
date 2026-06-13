import csv

def cargar_datos_csv():
    lista_paises = []
    try:
        with open("paises.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais_procesado = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais_procesado)
    except FileNotFoundError:
        print("Aviso: No se encontró el archivo 'paises.csv'. Se iniciará con la lista vacía.")
    return lista_paises

def mostrar_tabla_paises(lista):
    if not lista:
        print("No hay países cargados en el sistema.")
        return
        
    print(f"{'Nombre':<15} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente':<15}")
    print("-" * 65)
    for p in lista:
        print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<16} | {p['continente']:<15}")

def mostrar_menu():
    print("=====================================")
    print("  SISTEMA DE GESTIÓN DE PAÍSES UTN   ")
    print("=====================================")
    print("1. Mostrar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Guardar y Salir")

def menu_principal():
    paises = cargar_datos_csv() 
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            mostrar_tabla_paises(paises)
        elif opcion == "2":
            print("[Prueba] Elegiste: Agregar un país")
        elif opcion == "3":
            print("[Prueba] Elegiste: Actualizar datos")
        elif opcion == "4":
            print("[Prueba] Elegiste: Buscar país")
        elif opcion == "5":
            print("[Prueba] Elegiste: Filtrar países")
        elif opcion == "6":
            print("[Prueba] Elegiste: Ordenar países")
        elif opcion == "7":
            print("[Prueba] Elegiste: Mostrar estadísticas")
        elif opcion == "8":
            print("Saliendo del sistema... ¡Adiós!")
            continuar = False
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 8.")

if __name__ == "__main__":
    menu_principal()