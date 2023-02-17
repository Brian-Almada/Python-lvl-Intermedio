# Error Types

# SyntaxError --- Es el error de sintáxis


#print "Hola comunidad" --- error

# NameError

try:
    print(hola)
except:
    print("Este es un NameError que aparece cuando no definimos variables")

# IndexError

try:
    my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]

    print(my_list[5])
except:
    print("Este es un IndexError que aparece cuando le ponemos un indice de más o inexistente")

# ModuleNotFoundError

try:
    import maths
except:
    print("Este es un ModuleNotFoundError y aparece cuando no existe el archivo que importamos")

# AttributeError

import math
try:
    print(math.PI)
except:
    print("Este es un AttributeError y aparece cuando colocamos un atributo que no existe")

# KeyError

try:
    my_dick = {"name":"Brian", "surname":"Almada", "age":32, 1: "Python"}
    print(my_dick["aje"])
except:
    print("Este es un KeyError y aparece cuando colocamos una clave inexistente")

# TypeError

try:
    print(my_list["nombre"])
except:
    print("Este es un TypeError y aparece cuando usamos un tipo de valor no correspondiente")

# ImportError

try:
    from math import PI
except:
    print("Este es un ImportError y aparece cuando el nombre de lo que importamos es incorrecto")

# ValueError

try:
    my_int = int("10 años")
    print(type(my_int))
except:
    print("Este es un ValueError y aparece cuando pasamos un valor no correspondiente")

# ZeroDivisionError

try:
    print(4/0)
except:
    print("Este es un ZeroDivisionError y aparece cuando intentamos dividir un número por 0")