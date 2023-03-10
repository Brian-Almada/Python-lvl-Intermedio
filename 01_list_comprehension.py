# List Comprehension
# Son listas que se crean "sobre la marcha" a partir de un iterable

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list)

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)

# Ejemplos más complejos

# Podríamos crear una lista de esta manera sin usar listas de comprensión:

multiplos = []
for x in range(10):
    if x % 2 == 0:
        multiplos.append(x)

print(multiplos)

# O podemos crear esto mismo de una manera más optima usando listas por compresión:

multiplos = [x for x in range(10) if x % 2 == 0]
print(multiplos)


for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v,end = '')