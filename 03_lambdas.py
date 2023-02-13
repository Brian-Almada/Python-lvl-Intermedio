# Funciones Lambdas
# Una función lambda se define donde se usa, de esta manera no hay una función extra utilizando espacio en memoria. Si una función es utilizada una sola vez, lo mejor es usar una función lambda para evitar código innecesario y desorganizado

# La sintaxis de una función lambda es lambda args: expresión
#Una función lambda puede tener tantos argumento como necesites, pero debe tener una sola expresión.

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))