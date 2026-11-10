# Contar productos y consultar el conteo
# Categoría → cantidad de códigos.

from base import productos, normalizar

conteo = {}
for datos in productos.values():
    categoria = normalizar(datos["categoria"])
    conteo[categoria] = conteo.get(categoria, 0) + 1

categoria = "Escritura"
cantidad = conteo.get(normalizar(categoria), 0)
print(f"{categoria}: {cantidad} productos distintos")
