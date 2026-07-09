# TODO 1: crea el nombre "Cuaderno".
product_name = "Cuaderno"

# TODO 2: crea la categoría "Escolar".
category = "Escolar"

# TODO 3: crea el precio 7.5.
price = 7.5

# TODO 4: crea la cantidad 7.
quantity = 7

# TODO 5: multiplica price por quantity.
subtotal = price * quantity

# TODO 6: calcula cuántos paquetes completos de 3 unidades se pueden formar.
complete_packages = quantity // 3

# TODO 7: calcula cuántas unidades sobran después de formar los paquetes.
remaining_units = quantity % 3

# TODO 8: concatena product_name, " - " y category.
full_product_name = product_name + " - " + category

# TODO 9: obtiene el primer carácter de product_name.
first_character = product_name[0]

# TODO 10: obtiene los primeros cuatro caracteres de product_name.
first_four_characters = product_name[:4]

# TODO 11: convierte product_name a mayúsculas con upper().
uppercase_name = product_name.upper()

# TODO 12: crea la descripción "Cuaderno para clases".
description = "Cuaderno para clases"

# TODO 13: reemplaza "clases" por "dibujo" con replace().
modified_description = description.replace("clases", "dibujo")

# TODO 14: divide description en una lista de palabras con split().
description_words = description.split()

# TODO 15: muestra el subtotal.
print(subtotal)

# TODO 16: muestra la cantidad de paquetes completos.
print(complete_packages)

# TODO 17: muestra la cantidad de unidades sobrantes.
print(remaining_units)

# TODO 18: muestra el nombre completo del producto.
print(full_product_name)

# TODO 19: muestra el primer carácter.
print(first_character)

# TODO 20: muestra los primeros cuatro caracteres.
print(first_four_characters)

# TODO 21: muestra el nombre en mayúsculas.
print(uppercase_name)

# TODO 22: muestra la descripción modificada.
print(modified_description)

# TODO 23: muestra la lista de palabras.
print(description_words)
