# Consultar varios productos de un carrito
# Código → cantidad en el carrito; código → datos en el catálogo.

from base import productos

carrito = {"P001": 2, "P003": 1, "P005": 1, "P999": 1}
total = 0

for codigo, cantidad in carrito.items():
    producto = productos.get(codigo)
    if producto is None:
        print(codigo, "- Producto no encontrado")
    elif cantidad <= 0:
        print(codigo, "- La cantidad debe ser positiva")
    elif cantidad > producto["stock"]:
        print(codigo, "- Existencias insuficientes")
    else:
        subtotal = producto["precio"] * cantidad
        total += subtotal
        print(f"{codigo}: {cantidad} x "
              f"${producto['precio']:.2f} = ${subtotal:.2f}")

print(f"Total de partidas válidas: ${total:.2f}")
