import csv

def cargar_datos_csv():
    lista_paises = []
    try:
        with open("paises.csv", mode="r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
            if not lineas:
                return lista_paises

            for linea in lineas[1:]:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                
                if ";" in linea_limpia: # Para la coma y el punto y coma
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
                    
    except FileNotFoundError:
        print("AVISO! No se encontró el archivo 'paises.csv'. Se iniciará con la lista vacía.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        
    return lista_paises

def guardar_datos_csv(lista_paises): #Guarda datos nuevos en el archivo csv
    try:
        with open("paises.csv", mode="w", encoding="utf-8", newline="") as archivo:
            cabecera = ["nombre", "poblacion", "superficie", "continente"]
            lector = csv.DictWriter(archivo, fieldnames=cabecera)
            lector.writeheader()
            for pais in lista_paises:
                lector.writerow(pais)
        print("Los cambios fueron guardados en 'paises.csv' correctamente!")
    except Exception as e:
        print(f"ERROR! al intentar guardar el archivo: {e}")

def mostrar_tabla_paises(lista): #Muestra tabla de paises
    if not lista:
        print("No hay países para mostrar con ese criterio.")
        return
        
    print(f"\n{'Nombre':<15} | {'Población':<12} | {'Superficie (km²)':<16} | {'Continente':<15}")
    print("-" * 65)
    for p in lista:
        print(f"{p['nombre']:<15} | {p['poblacion']:<12} | {p['superficie']:<16} | {p['continente']:<15}")

def agregar_pais(lista_paises): #Ingreso de pais nuevo
    print("--- REGISTRAR NUEVO PAÍS ---")
    nombre = input("Ingrese el nombre del país: ").strip()
    if nombre == "":
        print("ERROR! El nombre no puede estar vacío.")
        return
        
    try:
        poblacion_input = input("Ingrese la cantidad de población: ").strip()
        if poblacion_input == "":
            print("ERROR! La población no puede estar vacía.")
            return
        poblacion = int(poblacion_input)
    except ValueError:
        print("ERROR! Debe ingresar un número entero válido.")
        return

    try:
        superficie_input = input("Ingrese la superficie en km²: ").strip()
        if superficie_input == "":
            print("ERROR! La superficie no puede estar vacía.")
            return
        superficie = int(superficie_input)
    except ValueError:
        print("ERROR! Debe ingresar un número entero válido.")
        return

    continente = input("Ingrese el continente al que pertenece: ").strip()
    if continente == "":
        print("ERROR! El continente no puede estar vacío.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    print(f"'{nombre}' fue agregado correctamente a la lista!")

def actualizar_pais(lista_paises): #Actualización de datos de paises ingresados
    print("--- ACTUALIZAR POBLACIÓN Y SUPERFICIE ---")
    nombre_buscar = input("Ingrese el nombre del país que desea modificar: ").strip().lower()
    pais_encontrado = None
    
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar:
            pais_encontrado = pais
            break

    if pais_encontrado is None:
        print(f"ERROR! No se encontró el país '{nombre_buscar}'.")
        return

    try:
        pais_encontrado["poblacion"] = int(input("Ingrese la NUEVA población: "))
        pais_encontrado["superficie"] = int(input("Ingrese la NUEVA superficie en km²: "))
        print("Datos actualizados en memoria!")
    except ValueError:
        print("ERROR! Entrada inválida. Operación cancelada.")

def buscar_pais(lista_paises): #Búsqueda de paises
    print("--- BUSCAR PAÍS ---")
    busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
    resultados = [p for p in lista_paises if busqueda in p["nombre"].lower()]
    mostrar_tabla_paises(resultados)

def filtrar_paises(lista_paises): #filtrado de paises con 3 criterios distintos
    if not lista_paises:
        print("No hay países cargados para filtrar.")
        return

    print("--- MENÚ DE FILTRADOS ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Población")
    print("3. Filtrar por Superficie")
    sub_opcion = input("Seleccione una opción de filtrado (1-3): ").strip()

    match sub_opcion:
        case "1": #Filtro por continente
            continente_buscar = input("Ingrese el continente por el cual filtrar: ").strip().lower()
            if continente_buscar == "":
                print("ERROR! El campo no puede estar vacío.")
                return
            resultados = [p for p in lista_paises if continente_buscar in p["continente"].lower()]
            print(f"Resultados para el continente '{continente_buscar}':")
            mostrar_tabla_paises(resultados)

        case "2": #Filtro por población
            try:
                limite_pob = int(input("Mostrar países con una población MAYOR a: "))
                if limite_pob < 0:
                    print("ERROR! El número no puede ser negativo.")
                    return
                resultados = [p for p in lista_paises if p["poblacion"] > limite_pob]
                print(f"Países con población mayor a {limite_pob}:")
                mostrar_tabla_paises(resultados)
            except ValueError:
                print("ERROR! Debe ingresar un número entero válido.")

        case "3": #Filtro por superficie
            try:
                limite_sup = int(input("Mostrar países con una superficie MAYOR a (en km²): "))
                if limite_sup < 0:
                    print("ERROR! El número no puede ser negativo.")
                    return
                resultados = [p for p in lista_paises if p["superficie"] > limite_sup]
                print(f"Países con superficie mayor a {limite_sup} km²:")
                mostrar_tabla_paises(resultados)
            except ValueError:
                print("ERROR! Debe ingresar un número entero válido.")
                
        case _:
            print("Opción de filtrado inválida. Volviendo al menú principal...")

def ordenar_paises(lista_paises): #Ordena la lista de paises por 3 criterios diferentes
    if not lista_paises:
        print("No hay países cargados para ordenar.")
        return

    print("--- MENÚ DE ORDENAMIENTO ---")
    print("1. Ordenar por Nombre (A-Z)")
    print("2. Ordenar por Población (Mayor a Menor)")
    print("3. Ordenar por Superficie (Mayor a Menor)")
    sub_opcion = input("Seleccione una opción de orden (1-3): ").strip()

    match sub_opcion:
        case "1": # Ordena alfabéticamente por 'nombre'
            lista_paises.sort(key=lambda x: x["nombre"].lower())
            print("¡Lista ordenada por Nombre de la A a la Z!")
            mostrar_tabla_paises(lista_paises)

        case "2": # Ordena por población
            lista_paises.sort(key=lambda x: x["poblacion"], reverse=True)
            print("¡Lista ordenada por Población de Mayor a Menor!")
            mostrar_tabla_paises(lista_paises)

        case "3": # Ordena por superficie
            lista_paises.sort(key=lambda x: x["superficie"], reverse=True)
            print("¡Lista ordenada por Superficie de Mayor a Menor!")
            mostrar_tabla_paises(lista_paises)

        case _:
            print("Opción de ordenamiento inválida. Volviendo al menú principal.")

def mostrar_estadisticas(lista_paises): #Calcula y muestra estadísticas
    if not lista_paises:
        print("No hay países cargados para calcular estadísticas.")
        return

    print("=====================================")
    print("   REPORTE ESTADÍSTICO DE PAÍSES     ")
    print("=====================================")

    # 1. Calcular Población Total
    # Sumamos la población de cada país usando una comprensión
    poblacion_total = sum(p[1] if isinstance(p, list) else p["poblacion"] for p in lista_paises)
    print(f"Población total mundial: {poblacion_total:,} habitantes".replace(",", "."))

    # 2. Calcular Promedio de Superficie
    superficie_total = sum(p[2] if isinstance(p, list) else p["superficie"] for p in lista_paises)
    promedio_superficie = superficie_total / len(lista_paises)
    print(f"Superficie promedio:     {promedio_superficie:,.2f} km²".replace(",", "X").replace(".", ",").replace("X", "."))

    # 3. Encontrar País con Mayor Población y Menor Superficie
    # Usamos la función max() y min() de Python que son súper potentes
    pais_mas_poblado = max(lista_paises, key=lambda x: x["poblacion"])
    pais_menos_superficie = min(lista_paises, key=lambda x: x["superficie"])

    print("-" * 37)
    print(f"País más poblado:        {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']:,} hab.)".replace(",", "."))
    print(f"País con menos área:     {pais_menos_superficie['nombre']} ({pais_menos_superficie['superficie']:,} km²)".replace(",", "."))

def mostrar_menu():
    print("=====================================")
    print("  SISTEMA DE GESTIÓN DE PAÍSES  ")
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
        
        match opcion:
            case "1":
                mostrar_tabla_paises(paises)
            case "2":
                agregar_pais(paises)
            case "3":
                actualizar_pais(paises)
            case "4":
                buscar_pais(paises)
            case "5":
                filtrar_paises(paises)
            case "6":
                ordenar_paises(paises)
            case "7":
                mostrar_estadisticas(paises)
            case "8":
                guardar_datos_csv(paises)
                print("\nSaliendo del sistema... ¡Adiós!")
                continuar = False
            case _:
                print("\nOpción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu_principal()