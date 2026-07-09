# TODO 1: crea una lista inicial con "lapiz", "cuaderno", "borrador" y "regla".
inventory = ["lapiz", "cuaderno", "borrador", "regla"]

# TODO 2: muestra el inventario inicial.
print("Inventario inicial:", inventory)

# TODO 3: obtiene el primer producto usando indice positivo.
first_product = inventory[0]

# TODO 4: obtiene el ultimo producto usando indice negativo.
last_product = inventory[-1]

# TODO 5: obtiene los productos centrales usando slicing.
middle_products = inventory[1:3]

# TODO 6: muestra el primer producto.
print("Primer producto:", first_product)

# TODO 7: muestra el ultimo producto.
print("Último producto:", last_product)

# TODO 8: muestra los productos centrales.
print("Productos centrales:", middle_products)

# TODO 9: modifica "cuaderno" por "agenda".
inventory[1] = "agenda"

# TODO 10: agrega "mochila" al final usando append().
inventory.append("mochila")

# TODO 11: inserta "plumon" en la posicion 2 usando insert().
inventory.insert(2, "plumon")

# TODO 12: agrega "colores" y "tijera" usando extend().
inventory.extend(["colores", "tijera"])

# TODO 13: elimina "borrador" usando remove().
inventory.remove("borrador")

# TODO 14: muestra el inventario actualizado.
print("Inventario actualizado:", inventory)

# TODO 15: vende el primer producto usando pop(0) y guardalo en sold_product.
sold_product = inventory.pop(0)

# TODO 16: comprueba si "regla" existe en el inventario.
has_rule = "regla" in inventory

# TODO 17: obtiene el indice de "regla".
rule_index = inventory.index("regla") if has_rule else -1

# TODO 18: obtiene la cantidad de productos.
product_count = len(inventory)

# TODO 19: obtiene los primeros tres productos usando slicing.
first_three = inventory[:3]

# TODO 20: obtiene los ultimos dos productos usando slicing.
last_two = inventory[-2:]

# TODO 21: muestra el producto vendido.
print("Producto vendido:", sold_product)

# TODO 22: muestra el inventario final.
print("Inventario final:", inventory)

# TODO 23: muestra si hay regla.
print("¿Hay regla?:", has_rule)

# TODO 24: muestra el indice de regla.
print("Índice de 'regla':", rule_index)

# TODO 25: muestra la cantidad de productos.
print("Cantidad de productos:", product_count)

# TODO 26: muestra los primeros tres productos.
print("Primeros tres productos:", first_three)

# TODO 27: muestra los ultimos dos productos.
print("Últimos dos productos:", last_two)

# TODO 28: muestra el titulo "Productos enumerados:".
print("Productos enumerados:")

# TODO 29: recorre inventory con enumerate(..., start=1) y muestra cada numero y producto.
for number, product in enumerate(inventory, start=1):
    print(number, product)
