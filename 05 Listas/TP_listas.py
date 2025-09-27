# 1. Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [4, 3, 5, 1, 2, 6, 7, 9, 8, 10]
suma = 0
promedio = 0

nota_minima = float('inf')
nota_maxima = float('-inf')

for i in range(len(notas)):
    print(notas[i])
    suma = suma + notas[i]
    promedio = suma / 10

    if notas[i] > nota_maxima:
        nota_maxima = notas[i]
    elif notas[i] < nota_minima:
        nota_minima = notas[i]

print("la nota mas alta es: ", nota_maxima)
print("la nota mas baja es: ", nota_minima)
print("el promedio de notas es: ", promedio)


# 2. Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []


while len(productos) < 5:
    print("Ingrese un producto a la lista de productos: ")
    prod = input()
    productos.append(prod)

print(sorted(productos))

print("¿Que producto desea eliminar de la lista?")
producto_eliminar = input()
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
else:
    print("El producto a eliminar no se encontró en la lista")

print(productos)


# 3. Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

random_lista = []

lista_pares = []

lista_impares = []

for i in range(15):
    num = random.randint(1,100)
    random_lista.append(num)
print(random_lista)

for num in random_lista:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)


print("La cantidad de numeros pares es: ", len(lista_pares))
print("La cantidad de numeros impares es: ", len(lista_impares))


# 4. Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_v2 = []

for elemento in datos:
    if elemento not in datos_v2:
        datos_v2.append(elemento)
print(datos_v2)


# 5. Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Facundo", "Julian", "Marcelo", "Alma", "Valentina", "Ramiro", "Antonella", "Tatiana"]
print(estudiantes)
print()
print("Escribe la opcion que deseas realizar respecto a los estudiantes")
print("opcion A: agregar estudiante a la lista.")
print("opcion B: eliminar estudiante de la lista.")

opcion = input()

if opcion.lower() == "a":
    print("Ingrese el nombre del estudiante: ")
    estudiante = input()
    estudiantes.append(estudiante)
elif opcion.lower() == "b":
    print("ingrese a que estudiante de la lista que desea eliminar")
    eliminar = input()
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
else:
    print("la letra ingresada no se encuentra entre las opciones indicadas.")

print(estudiantes)


# 6. Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero). 

lista = [6, 4, 6, 1, 7, 3, 8]

ultimo_elemento = lista.pop()
lista.insert(0, ultimo_elemento)

print(lista)


# 7. Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [12, 25],
    [14, 28],
    [10, 22],
    [16, 30],
    [13, 27],
    [11, 20],
    [15, 29]
]

suma_min = 0
suma_max = 0

for dia in temperaturas:
    suma_min = suma_min + dia[0]
    suma_max = suma_max + dia[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print("El promedio de minimas es: ", promedio_min)
print("El promedio de maximas es: ", promedio_max)

mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud = maxima - minima

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1 

print("la mayor amplitud termica fue el dia ", dia_mayor_amplitud, "con ", mayor_amplitud,"°C")


# 8. Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [6, 7, 5],
    [8, 9, 7]
]

print("Promedios por estudiante:")
for i in range(len(notas)):
    promedio_estudiante = sum(notas[i]) / len(notas[i])
    print(f"estudiante {i+1}: {promedio_estudiante}")

print("Promedios por materia:")
num_materias = len(notas[0])  # [7, 8, 6]

for j in range(num_materias):
    suma = 0
    for i in range(len(notas)):
        suma = suma + notas[i][j]
    promedio_materia = suma / len(notas)
    print(f"Materia {j+1}: {promedio_materia}")


# 9. Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("Tablero inicial:")
for fila in tablero:
    print(fila)

jugador = "X"

jugadas = 0
while jugadas < 9:
    print(f"\nTurno del jugador {jugador}")

    fila = int(input("Ingresa la fila (0, 1 o 2): "))
    columna = int(input("Ingresa la columna (0, 1 o 2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas = jugadas + 1
    else:
        print("Esa casilla ya está ocupada. Intenta de nuevo.")
        continue 

    for fila_tablero in tablero:
        print(fila_tablero)

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"
# 10. Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 15, 20, 12, 18, 25, 30],   # Producto 1
    [5,  8,  12, 9,  7,  10, 15],   # Producto 2
    [20, 22, 18, 25, 30, 28, 35],   # Producto 3
    [12, 14, 16, 13, 15, 19, 20]    # Producto 4
]

print("Total vendido por cada producto:")
for i in range(len(ventas)):  
    total_producto = sum(ventas[i])
    print(f"Producto {i+1}: {total_producto}")

print("\nDía con mayores ventas totales:")
num_dias = len(ventas[0]) 
mayor_ventas = 0
dia_mayor = 0

for j in range(num_dias):
    suma_dia = 0
    for i in range(len(ventas)):
        suma_dia = suma_dia + ventas[i][j]
    print(f"Día {j+1}: {suma_dia}")

    if suma_dia > mayor_ventas:
        mayor_ventas = suma_dia
        dia_mayor = j+1

print(f"El día con más ventas fue el Día {dia_mayor} con {mayor_ventas} unidades.")

print("\nProducto más vendido en la semana:")
mas_vendido = 0
producto_mas_vendido = 0

for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    if total_producto > mas_vendido:
        mas_vendido = total_producto
        producto_mas_vendido = i+1

print(f"El producto más vendido fue el Producto {producto_mas_vendido} con {mas_vendido} unidades.")
