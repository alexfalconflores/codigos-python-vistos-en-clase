# TODO 1: solicita la edad. input() devuelve un str.
age_text = input("Ingresa tu edad: ")

# TODO 2: convierte age_text de str a int.
age = int(age_text)

# TODO 3: solicita la estatura. input() devuelve un str.
height_text = input("Ingresa tu estatura (por ejemplo 1.75): ")

# TODO 4: convierte height_text de str a float.
height = float(height_text)

# TODO 5: crea un puntaje int con el valor 15.
score = 15

# TODO 6: crea una bonificación float con el valor 2.5.
bonus = 2.5

# TODO 7: suma score y bonus. Python realizará una conversión implícita.
final_score = score + bonus

# TODO 8: convierte age a str y crea el mensaje "Edad: 20".
age_message = "Edad: " + str(age)

# TODO 9: crea una lista con "Python" y "Git".
course_list = ["Python", "Git"]

# TODO 10: convierte course_list a tuple.
course_tuple = tuple(course_list)

# TODO 11: muestra el valor y el tipo de age.
print(age, type(age))

# TODO 12: muestra el valor y el tipo de height.
print(height, type(height))

# TODO 13: muestra el valor y el tipo de final_score.
print(final_score, type(final_score))

# TODO 14: muestra el valor y el tipo de age_message.
print(age_message, type(age_message))

# TODO 15: muestra el valor y el tipo de course_tuple.
print(course_tuple, type(course_tuple))
