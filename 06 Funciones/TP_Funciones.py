# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

ingrese_nombre = input("Ingrese su nombre: ")
print(saludar_usuario(ingrese_nombre))


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

ingrese_nombre = input("Ingrese su nombre: ")
ingrese_apellido = input("Ingrese su apellido: ")
ingrese_edad = int(input("Ingrese su edad: "))
ingrese_residencia = input("Ingrese su país de residencia: ")

print(informacion_personal(ingrese_nombre, ingrese_apellido, ingrese_edad, ingrese_residencia))


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.1416 * (radio**2)

def calcular_perimetro_circulo(radio):
    return radio * 2 * 3.1416

ingrese_radio = float(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es: {calcular_area_circulo(ingrese_radio)} y el perimetro es: {calcular_perimetro_circulo(ingrese_radio)}")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 60

ingrese_segundos = int(input("Ingrese la cantidad de segundos que desee convertir a horas: "))
print(f"los segundos ingresados, expresados en horas serian: {segundos_a_horas(ingrese_segundos)} horas.")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

ingrese_numero = int(input("Ingrese un numero: "))
tabla_multiplicar(ingrese_numero)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b 
    division = a / b 
    return (suma, resta, multiplicacion, division)

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

ingrese_peso = float(input("Ingrese su peso: "))
ingrese_altura = float(input("Ingrese su altura: "))

print(f"Su Indice de Masa Corporal (IMC) es: {calcular_imc(ingrese_peso, ingrese_altura):.2f}")


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    far = (celsius * 9/5) + 32
    return far

ingrese_celsius = float(input("Ingrese grados celsius: "))
print(f"los grados celsius ingreados equivalen a {celsius_a_fahrenheit(ingrese_celsius)} grados fahrenheit")


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3 

print("Ingrese 3 numeros para calcular el promedio de los mismos.")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los numeros ingresados es {promedio:.2f}")