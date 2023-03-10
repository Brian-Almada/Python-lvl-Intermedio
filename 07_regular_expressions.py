# Regular Expressions

import re

my_string = "Esta es la lección número 7. Lección llamada: Expresiones Regulares"

my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

#match

print(re.match("Esta es la lección", my_string)) # match reconoce si hay algún patrón en el string
print(re.match("Esta es la lección", my_other_string))# Aquí nos dice que esta porción de texto no se encuentra en la variable my_other_string
print(re.match("Expresiones Regulares", my_string)) # Dice none porque match comienza a buscar desde el principio.

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = print(re.match("Esta es la lección", my_other_string))
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_string[start:end])

#search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall) # Este objeto permite encontrar todas las instancias de la palabra o palabras que queremos encontrar

# split

print(re.split("a", my_string))
print(re.split(":", my_string)) # El objeto split lo que hace es colocar el texto en una lista y separarlo en las porciones desde el patrón que le coloquemos sin tener en cuenta dicho patrón cuando lo coloca en la lista.

# sub

print(re.sub("Expresiones Regulares", "RegEx", my_string)) # Sub lo que hace es substituir la cadena o palabra que le pasamos en el primer parámetro por la cadena o palabra que le pasamos en el segundo parámetro

# Patterns

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email = 'brianalexis@gmail.com'

print(re.findall(pattern, email))