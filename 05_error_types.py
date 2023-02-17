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