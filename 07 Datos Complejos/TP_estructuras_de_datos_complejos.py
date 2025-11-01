# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precio_frutas = {
    'Banana' : 1200,
    'Anana' : 2500,
    'Melon' : 3000,
    'Uva' : 1450
}

# print(precio_frutas)

precio_frutas['Naranja'] = 1200
precio_frutas['Manzana'] = 1500
precio_frutas['Pera'] = 2300

# print(precio_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precio_frutas['Banana'] = 1330
precio_frutas['Manzana'] = 1700
precio_frutas['Melon'] = 2800

# print(precio_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_frutas = list(precio_frutas.keys())
print(lista_frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

while len(contactos) < 5:
    nombre = input("Ingrese el nombre del contacto: ")
    num = input("Ingrese el numero de contacto: ")
    contactos[nombre] = num

buscar_contacto = input("Ingrese el nombre del contacto que desea buscar: ")
if buscar_contacto in contactos:
    print(f"el numero de telefono de {buscar_contacto} es: {contactos[buscar_contacto]}")
else: 
    print("el contacto no existe")


# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()
print(f"Lista generada a partir de la frase: {palabras}")
palabras_unicas = set(palabras)
print(f"Lista de palabras únicas: {palabras_unicas}")

dic_palabras = {}

for palabra in palabras:
    if palabra in dic_palabras:
        dic_palabras[palabra] += 1
    else:
        dic_palabras[palabra] = 1

print(dic_palabras)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

def tupla_notas(nota1, nota2, nota3):
    return (nota1, nota2, nota3)

alumnos = {}

while len(alumnos) < 3:
    nombre = input("Ingrese el nombre del alumno: ")
    n1 = float(input("Ingrese la primer nota: "))
    n2 = float(input("Ingrese la segunda nota: "))
    n3 = float(input("Ingrese la tercer nota: "))
    alumnos[nombre] = tupla_notas(n1, n2, n3)


for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio del alumno {nombre} es: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 5, 7, 8, 9, 11, 12, 14, 16, 18, 20}
parcial2 = {1, 2, 3, 4, 5, 8, 10, 11, 13, 15, 16, 17, 18, 19, 20}

ambos_parciales = parcial1 & parcial2
un_parcial = parcial1 ^ parcial2
al_menos_un_parcial = parcial1 | parcial2

print(f"Los alumnos que aprobaron ambos parciales son: {ambos_parciales}")
print(f"Los alumnos que aprobaron un parcial son: {un_parcial}")
print(f"Los alumnos que aprobaron al menos un parcial son: {al_menos_un_parcial}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

productos = {
    'pantalones' : 0,
    'camisetas' : 0,
    'buzos' : 0
}

consultar_stock = input("Ingrese el nombre del producto del cual quiere consultar el stock: ").lower()
if consultar_stock in productos:
    print(f"El stock del producto es: {productos[consultar_stock]}")
    s_n = input(("¿Quiere ingresar stock al producto? S/N: ")).lower()
    if s_n == "s":
        agregar_unidades = int(input("Ingrese el stock del producto: "))
        productos[consultar_stock] += agregar_unidades
        print(f"El stock del producto actualizado es: {productos[consultar_stock]}")
else: 
    productos[consultar_stock] = 0
    print(f"El producto {consultar_stock} no existia y fue agregado exitosamente.")
    agregar_unidades = int(input("Ingrese el stock del producto: "))
    productos[consultar_stock] += agregar_unidades
    print(f"El stock del nuevo producto es: {productos[consultar_stock]}")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ('lunes', '15:30') : 'Reunion de Padres',
    ('sabado', '07:00') : 'Parcial de Programacion I'
}

dia = input("Ingrese el dia de la agenda que desee consultar: ").lower()
hora = input("Ingrese la hora del dia que desee consultar: ")

dia_hora = (dia, hora)

if dia_hora in agenda:
    print(f"el dia {dia} a las {hora}hs, tiene agendado: {agenda[dia_hora]}")
else:
    print("No tiene nada agendado para la fecha y el horario ingresado.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {
    'Argentina' : 'Buenos Aires',
    'Francia' : 'Paris',
    'Noruega' : 'Oslo',
    'Suecia' : 'Estocolmo'
}
print(original)

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)