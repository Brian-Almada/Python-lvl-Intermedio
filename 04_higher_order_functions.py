# Higher Order Functions
# Una función se denomina Función de orden superior si esta contiene otras funciones como parámetros de entrada o si devuelve una función como salida

def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(5, 2))