# Funciones Lambdas
# Una función lambda se define donde se usa, de esta manera no hay una función extra utilizando espacio en memoria. Si una función es utilizada una sola vez, lo mejor es usar una función lambda para evitar código innecesario y desorganizado

# La sintaxis de una función lambda es lambda args: expresión
#Una función lambda puede tener tantos argumento como necesites, pero debe tener una sola expresión.

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

# Funciones que retornan lambdas:

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))

# Solo es necesario una función lambada y se puede retornar en 3 operaciones distintas
def multiplicar_por(n):
    return lambda x: x * n

duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)

print(duplicar(6))
print(triplicar(2))
print(diez_veces(1000))