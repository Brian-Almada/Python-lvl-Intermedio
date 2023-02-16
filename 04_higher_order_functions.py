# Higher Order Functions
# Una función se denomina Función de orden superior si esta contiene otras funciones como parámetros de entrada o si devuelve una función como salida

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

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))