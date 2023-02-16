# Higher Order Functions
# Una función se denomina Función de orden superior si esta contiene otras funciones como parámetros de entrada o si devuelve una función como salida

from functools import reduce

def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(5, 2))


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

# Closures
# Las clausuras son funciones que dentro de ellas encierran a otra función y a su ámbito de aplicación, lo que permite el acceso a variables definidas dentro de la función interna, incluso fuera de su ámbito. Una clausura siempre retorna la función que define dentro.

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

# Built-in Higher ORder Functions

numbers = [2, 5, 10, 21]

#Map
# El map recorre todos los valores y ejecuta una función sobre ellos para modificar su valor

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
#el filter recorre todos los valores y ejecuta una función que retorna True o False para saver como filtrar los valores

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
# Reduce nos retorna el acumulado de la lista. En este caso suma el primer valor con el segundo (2 + 5 = 7) El 7 termina siendo el primer valor y lo suma con el segundo que sigue que es 10 (7 + 10 = 17) 17 se convierte en el first_value y se suma con el second_value que sigue que es 21 (17 + 21 = 38) Es por eso que el resultado de reduce es 38

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))
