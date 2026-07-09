import math


# TODO 1: crea infinito positivo usando float().
positive_infinity = float("inf")

# TODO 2: crea infinito negativo usando float().
negative_infinity = float("-inf")

# TODO 3: crea un valor NaN usando float().
not_a_number = float("nan")

# TODO 4: suma 100 a positive_infinity.
infinity_plus_100 = positive_infinity + 100

# TODO 5: resta positive_infinity de positive_infinity.
indeterminate_subtraction = positive_infinity - positive_infinity

# TODO 6: multiplica 0 por positive_infinity.
indeterminate_multiplication = 0 * positive_infinity

# TODO 7: comprueba con math.isinf() si positive_infinity es infinito.
is_infinity = math.isinf(positive_infinity)

# TODO 8: comprueba con math.isnan() si not_a_number es NaN.
is_nan = math.isnan(not_a_number)

# TODO 9: compara not_a_number consigo mismo usando ==.
nan_equals_itself = (not_a_number == not_a_number)

# TODO 10: muestra el infinito positivo.
print(positive_infinity)

# TODO 11: muestra el infinito negativo.
print(negative_infinity)

# TODO 12: muestra el valor NaN.
print(not_a_number)

# TODO 13: muestra el resultado de infinito más 100.
print(infinity_plus_100)

# TODO 14: muestra el resultado de infinito menos infinito.
print(indeterminate_subtraction)

# TODO 15: muestra el resultado de cero por infinito.
print(indeterminate_multiplication)

# TODO 16: muestra el resultado de math.isinf().
print(is_infinity)

# TODO 17: muestra el resultado de math.isnan().
print(is_nan)

# TODO 18: muestra el resultado de comparar NaN consigo mismo.
print(nan_equals_itself)
