# Buscar y actualizar existencias
# Se utiliza el índice principal por código.

from base import productos, mostrar

codigo = "P005"
entrada = 10
producto = productos.get(codigo)

if producto is None:
    print("Producto no encontrado")
else:
    print("Antes:")
    mostrar(codigo)
    producto["stock"] += entrada
    print("Después de agregar", entrada, "unidades:")
    mostrar(codigo)
