#1
print("Hola Mundo!")

#2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3
nombre = input("ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
residencia = input("Ingrese su país de residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4
radio = float(input("Ingrese el radio del circulo "))
area = 3.1416 * radio * radio
perimetro = 2 * 3.1416 * radio
print(f"el area del circulo es {area} y el perimetro es {perimetro}")

#5
segundos = int(input("Ingrese una cantidad de segundos "))
horas = segundos / 60
print(f"la cantidad de segundos ingresadas seria en horas: {horas}")

#6
num = int(input("Ingrese un numero "))
print(f"la tabla de multiplicar de ese numero es la siguiente:")
print(f"{num} x 1 = ", num*1)
print(f"{num} x 2 = ", num*2)
print(f"{num} x 3 = ", num*3)
print(f"{num} x 4 = ", num*4)
print(f"{num} x 5 = ", num*5)
print(f"{num} x 6 = ", num*6)
print(f"{num} x 7 = ", num*7)
print(f"{num} x 8 = ", num*8)
print(f"{num} x 9 = ", num*9)
print(f"{num} x 10 = ", num*10)

#7
num1 = int(input("ingrese un numero distinto a 0 "))
num2 = int(input("ingrese otro numero distinto a 0 "))
print(f"la suma de los numeros ingresados es:", num1 + num2)
print(f"la division de los numeros ingresados es:", num1 / num2)
print(f"la multiplicacion de los numeros ingresados es:", num1 * num2)
print(f"la resta de los numeros ingresados es:", num1 - num2)

#8
altura = float(input("ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
print(f"su Indice de Masa Corporal (IMC) es:", peso / (altura * altura))

#9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = float(celsius * (9/5)+32)
print(f"la temperatura ingresada en celsius serian {fahrenheit} grados Fahrenheit")

#10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los 3 numeros ingresados es {promedio}")