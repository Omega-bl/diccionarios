# Catálogo de ejemplo de una papelería.
# Clave: código del producto. Valor: diccionario con sus datos.

productos = {
    "P001": {"nombre": "Lápiz HB", "categoria": "Escritura",
             "precio": 6.50, "stock": 50, "proveedor": "Norte"},
    "P002": {"nombre": "Bolígrafo azul", "categoria": "Escritura",
             "precio": 8.00, "stock": 40, "proveedor": "Norte"},
    "P003": {"nombre": "Cuaderno profesional", "categoria": "Cuadernos",
             "precio": 35.00, "stock": 25, "proveedor": "Centro"},
    "P004": {"nombre": "Cuaderno de dibujo", "categoria": "Cuadernos",
             "precio": 28.00, "stock": 12, "proveedor": "Centro"},
    "P005": {"nombre": "Borrador", "categoria": "Accesorios",
             "precio": 5.00, "stock": 0, "proveedor": "Norte"},
    "P006": {"nombre": "Regla de 30 cm", "categoria": "Accesorios",
             "precio": 12.00, "stock": 15, "proveedor": "Sur"},
    "P007": {"nombre": "Marcadores de colores", "categoria": "Arte",
             "precio": 48.00, "stock": 8, "proveedor": "Sur"},
    "P008": {"nombre": "Cartulina blanca", "categoria": "Arte",
             "precio": 7.00, "stock": 30, "proveedor": "Centro"},
    "P009": {"nombre": "Lápiz de color", "categoria": "Arte",
             "precio": 10.00, "stock": 0, "proveedor": "Sur"},
    "P010": {"nombre": "Bolígrafo azul", "categoria": "Escritura",
             "precio": 9.50, "stock": 18, "proveedor": "Centro"},
}


def normalizar(texto):
    # Ignora mayúsculas y espacios de los extremos; conserva acentos.
    return texto.strip().casefold()


def mostrar(codigo):
    producto = productos.get(codigo)
    if producto is None:
        print(codigo, "- Producto no encontrado")
    else:
        print(f"{codigo} - {producto['nombre']} | "
              f"${producto['precio']:.2f} | "
              f"Existencias: {producto['stock']}")


if __name__ == "__main__":
    print("CATÁLOGO DE LA PAPELERÍA")
    for codigo in productos:
        mostrar(codigo)
