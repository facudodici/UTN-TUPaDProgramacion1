# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#solicito al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))
#creo la condicion, si es igual o mayor a 18 imprimo "es mayor de edad"
if edad >= 18:
    print("Es mayor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

#solicito al usuario que ingrese la nota
nota = float(input("Ingrese su nota: "))
#si la nota es mayor o igual a 6 imprimo "aprobado" sino imprimo "desaprobado"
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

print("Este programa solo permite el ingreso de numeros pares")
#solicito al usuario que ingrese un numero
num = int(input("Ingrese un numero: "))
#si el numero es par imprimo "Ha ingresado un numero par", sino imprimo "por favor, ingrese un numero par"
if (num % 2) == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
#Solicito la edad al usuario
edad = int(input("Ingrese su edad: "))
#si es mejor de 12 años es un niño.
if edad < 12:
    print("Categoría: Niño")
#si es mayor o igual que 12 o menor que 18 es adolescente.
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
#si es mayor o igual que 18 o mejor que 30 es adulto/a joven.
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a Joven")
else:
    print("Categoría: Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
#Solicito al usuario que ingrese una contraseña que contenga entre 8 y 14 caracteres
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
#si la cantidad de digitos de la contraseña es mayor o igual a 8 Y menor o igual a 14 imprimo "ha ingresado una contraseña correcta"
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
#sino imprimo que ingrese una contraseña de entre 8 y 14 digitos
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6
##PERDON, NO ENTENDI ESTE EJERCICIO. (PEDI AYUDA A CHAT GPT PERO TAMPOCO LO ENTENDI Y NO QUIERO QUE ME LO RESUELVA LA INTELIGENCIA ARTIFICIAL)


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
#solicito palabra/frase usando el metodo .lower() investigado personalmente con chatGPT
palabra = input("Ingrese una palabra o una frase ").lower()
#Consulto si la ultima letra de la palabra finaliza con vocal utilizando el indice negativo -1
if palabra[-1] in "aeiou":
    #imprimo la palabra concatenandole el signo de exclamacion
    print(f"{palabra}!")
else:
    print(f"{palabra}")


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
#solicito el nombre
nombre = input("Ingrese su nombre: ")
#doy a elegir las opciones
print("Ingrese un numero dependiendo la opción deseada")
print("#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
num = int(input("Ingrese la opción escogida: "))
#si el numero es el 1 uso la funcion upper()
if num == 1:
    print(nombre.upper())
#si el numero es el 2 uso lower()
elif num == 2: 
    print(nombre.lower())
#sino uso title()
else:
    print(nombre.title())


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Categoría: Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Categoría: Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Categoría: Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Categoría: Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Categoría: Muy Fuerte (puede causar daños significativos)")
else:
    print("Categoría: Extremo (puede causar graves daños a gran escala)")


#10)
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}
# Pedir datos al usuario
hemisferio = input("Ingrese en qué hemisferio se encuentra (N/S): ").upper()
mes = input("Ingrese el mes del año (ej: marzo): ").lower()
dia = int(input("Ingrese el día del mes (1-31): "))
# Convertir mes a número
mes = meses[mes]
# Determinar estación
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"
else:
    estacion = "Fecha inválida"
print(f"Usted se encuentra en {estacion}.")