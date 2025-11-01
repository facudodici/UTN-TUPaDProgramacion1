# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write('lapicera, 250, 50\n')
    archivo.write('lapiz, 100, 150\n')
    archivo.write('cartuchera, 1500, 25\n')

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto
# (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.


with open("productos.txt", "a") as archivo:
    nombre = input("Ingrese el nombre del producto que desea ingresar: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad de unidades: ")
    archivo.write(f'{nombre}, {precio}, {cantidad}\n')


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos,
# donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    productos = []
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        diccionario = {
            'nombre' : nombre,
            'precio' : precio,
            'cantidad' : cantidad
        }
        productos.append(diccionario)

print(productos)

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos.
# Si no existe, mostrar un mensaje de error.

prod = input("Ingrese el nombre del producto que desea buscar: ").lower()

for producto in productos:
    if prod == producto["nombre"]:
        print(producto)

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt
# escribiendo nuevamente todos los productos actualizados desde la lista.

listas_act = []
for producto in productos:
    linea = f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n"
    listas_act.append(linea)

with open("productos.txt", "w") as archivo:
    archivo.writelines(listas_act)