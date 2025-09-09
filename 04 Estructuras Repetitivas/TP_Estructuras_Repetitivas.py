#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (101):
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un numero: "))
contador = 0
if num < 0:
    print("Debía ingresar un numero mayor a cero")
elif num == 0:
    contador = 1
else:
    while num > 0:
        num //= 10
        contador += 1
print("la cantidad de digitos que contiene el numero es:", contador)


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

menor = 0 
mayor = 0

if num1 == num2:
    print("No hay numeros que sumar")
elif num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

suma = 0

for i in range (menor + 1, mayor):
    suma = suma + i

print("la suma de los numeros enteros comprendidos entre los numeros dados por el usuario es:", suma)
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
num = int(input("Ingrese un numero: "))
while num != 0:
    suma = suma + num
    num = int(input("Ingresa otro numero: "))
print("la suma de los numeros ingresados es: ", suma)
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_aleatorio = random.randint(0,9)
cont_intentos = 1

num = int(input("Ingrese un numero entre 0 y 9: "))

while num != num_aleatorio:
    print("Intenta nuevamente")
    num = int(input("Ingrese un nuevo numero: "))
    cont_intentos = cont_intentos + 1
    
print("ADIVINASTE!, lo resolviste en", cont_intentos, "intentos!")
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range (100,-1,-2):
    print(i)
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero: "))

if num <= 0:
    print("El numero debe ser positivo")
else:
    suma = 0
    for i in range (0,num+1):
        suma += i
    print("La suma de todos los numeros comprendidos entre el 0 y el numero ingresado es:", suma)
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range (100):
    print("Ingrese un numero: ")
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0 :
        negativos += 1
print("la cantidad de numeros pares son:", pares, ", la cantidad de impares son:", impares, ", la cantidad de positivos son:", positivos, " y la cantidad de negativos son:", negativos)
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0

for i in range (10):
    print("Ingrese un numero: ")
    num = int(input())
    suma += num

media = suma / 10
print("La media de los valores ingresados es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero "))

num_inv = str(num)[::-1] #

print("El numero invertido es:", num_inv)