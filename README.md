# TPI_P1
Trabajo Práctico Integrador | Programación 1 | UTN 1C 2026

# Integrantes del grupo:
**Leila Magalí Bruno** - Comisión: 14 |
**Lucia Victoria Ledesma** - Comisión: 5 

# Sistema de Gestión de Datos de Países en Python
Este proyecto es el Trabajo Práctico Integrador para la materia Programación 1 de la Tecnicatura Universitaria en Programación a Distancia de la Universidad Tecnológica Nacional.
El sistema consiste en una aplicación de consola desarrollada en Python que permite gestionar, filtrar, ordenar y obtener estadísticas de un dataset de países almacenado en formato CSV.

# Arquitectura y Estructuras de Datos Utilizadas
Para el desarrollo de la solución, se priorizó la robustez del código y la implementación de características del lenguaje Python:

**Colecciones:** Al iniciar la aplicación, los datos del archivo físico se cargan dinámicamente en una lista de diccionarios. Cada diccionario representa un país estructurado bajo las claves `nombre`, `poblacion`, `superficie` y `continente`. 
Esta estructura garantiza mutabilidad y un acceso indexado eficiente a los campos.
**Estructura de Control (`match-case`):** Tanto el flujo del menú principal como los submenús de filtrado y ordenamiento se resolvieron utilizando la estructura de coincidencia de patrones match-case. Esto asegura un código limpio, modular, escalable y con mayor legibilidad.
***Comprensión de Listas:** Se utilizaron expresiones compactas para procesar los filtros y búsquedas, optimizando el rendimiento al generar subconjuntos de datos filtrados en una sola línea de ejecución de manera altamente eficiente.
**Funciones Lambda:** Se implementaron expresiones anónimas (`lambda`) como criterios de ordenamiento (`key`) dentro del método `.sort()`, logrando reorganizar los registros en memoria de forma dinámica según valores alfabéticos o numéricos.

# Funcionalidades del Sistema
El programa cuenta con un menú interactivo en consola que incluye:
**Mostrar todos los países:** Lectura directa y formateo del archivo de datos.
**Agregar un país:** Validación de campos obligatorios no vacíos.
**Actualizar datos:** Modificación de población y superficie buscando por coincidencia exacta de nombre.
**Buscar país:** Búsqueda por coincidencia parcial o exacta.
**Filtrar países:** Por continente, rango de población o rango de superficie.
**Ordenar países:** Por nombre, población o superficie de forma ascendente o descendente.
**Estadísticas avanzadas:** País con mayor/menor población, promedios globales y conteo por continente.

# Video Demostración e Informe PDF
**Enlace al Video Explicativo:** [https://drive.google.com/drive/folders/1YQ-9wOPluPTvBhdS6Tw3STNu2WLVC2Bz] |
**Documentación Académica:** []

