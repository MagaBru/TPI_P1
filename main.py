import csv

def cargar_datos_csv():
    """Lee el archivo 'paises.csv'."""
    lista_paises = []
    try:
        # === BLOQUE DE DIAGNÓSTICO (Para espiar el archivo por dentro) ===
        try:
            with open("paises.csv", mode="r", encoding="utf-8") as f:
                print("\n========================================")
                print(f.read())
                print("========================================")
        except FileNotFoundError:
            print("\nAviso: Físicamente no existe el archivo 'paises.csv' en esta carpeta.")
            return lista_paises
        # =================================================================

        # Procesamiento real del archivo
        with open("paises.csv", mode="r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
            if not lineas:
                return lista_paises

            # Recorremos saltando la cabecera
            for linea in lineas[1:]:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                
                # Detectamos si usa coma o punto y coma
                if ";" in linea_limpia:
                    columnas = linea_limpia.split(";")
                else:
                    columnas = linea_limpia.split(",")
                
                if len(columnas) < 4:
                    continue
                
                try:
                    pais_procesado = {
                        "nombre": columnas[0].strip(),
                        "poblacion": int(columnas[1].strip()),
                        "superficie": int(columnas[2].strip()),
                        "continente": columnas[3].strip()
                    }
                    lista_paises.append(pais_procesado)
                except ValueError:
                    continue
                    
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        
    return lista_paises

def mostrar_tabla_paises(lista):
    """Muestra los países formateados como una tabla limpia en consola."""
    if not lista:
        print("\nNo hay países cargados en el sistema para mostrar.")
        return
        
    print(f"\n{'Nombre':<15} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente':<15}")
    print("-" * 65)
    for p in lista:
        print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<16} | {p['continente']:<15}")

def agregar_pais(lista_paises):
    """Agrega un nuevo país validando que no haya campos vacíos."""
    print("\n--- REGISTRAR NUEVO PAÍS ---")
    nombre = input("Ingrese el nombre del país: ").strip()
    if nombre == "":
        print("Error: El nombre no puede estar vacío.")
        return
        
    try:
        poblacion_input = input("Ingrese la cantidad de población: ").strip()
        if poblacion_input == "":
            print("Error: La población no puede estar vacía.")
            return
        poblacion = int(poblacion_input)
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    try:
        superficie_input = input("Ingrese la superficie en km²: ").strip()
        if superficie_input == "":
            print("Error: La superficie no puede estar vacía.")
            return
        superficie = int(superficie_input)
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    continente = input("Ingrese el continente al que pertenece: ").strip()
    if continente == "":
        print("Error: El continente no puede estar vacío.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    print(f"\n¡Éxito! '{nombre}' fue agregado correctamente.")

def actualizar_pais(lista_paises):
    print("\n--- ACTUALIZAR POBLACIÓN Y SUPERFICIE ---")
    nombre_buscar = input("Ingrese el nombre del país que desea modificar: ").strip().lower()
    pais_encontrado = None
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar:
            pais_encontrado = pais
            break

    if pais_encontrado is None:
        print(f"Error: No se encontró el país '{nombre_buscar}'.")
        return

    try:
        pais_encontrado["poblacion"] = int(input("Ingrese la NUEVA población: "))
        pais_encontrado["superficie"] = int(input("Ingrese la NUEVA superficie en km²: "))
        print("\n¡Éxito! Datos actualizados en memoria.")
    except ValueError:
        print("Error: Entrada inválida. Operación cancelada.")

def buscar_pais(lista_paises):
    print("\n--- BUSCAR PAÍS ---")
    busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
    resultados = [p for p in lista_paises if busqueda in p["nombre"].lower()]
    mostrar_tabla_paises(resultados)

def guardar_datos_csv(lista_paises):
    """Toma la lista de memoria y la sobreescribe en el archivo paises.csv para salvar los cambios."""
    try:
        with open("paises.csv", mode="w", encoding="utf-8", newline="") as archivo:
            # Definimos los nombres de las columnas idénticos a como estaban
            cabecera = ["nombre", "poblacion", "superficie", "continente"]
            lector = csv.DictWriter(archivo, fieldnames=cabecera)
            
            # Escribimos los títulos arriba de todo
            lector.writeheader()
            
            # Mandamos todos los países de nuestra lista
            for pais in lista_paises:
                lector.writerow(pais)
                
        print("\n[Éxito] ¡Todos los cambios fueron guardados en 'paises.csv' correctamente!")
    except Exception as e:
        print(f"\nError crítico al intentar guardar el archivo: {e}")

def mostrar_menu():
    print("\n=====================================")
    print("  SISTEMA DE GESTIÓN DE PAÍSES UTN   ")
    print("=====================================")
    print("1. Mostrar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie")
    print("4. Buscar país por nombre")
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
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "8":
            guardar_datos_csv(paises) # <--- ¡Clave! Primero guarda los cambios en el archivo...
            print("\nSaliendo del sistema... ¡Adiós!")
            continuar = False # <--- ...y después rompe el bucle para cerrar el programa.
        else:
            print("\nOpción inválida.")

if __name__ == "__main__":
    menu_principal()