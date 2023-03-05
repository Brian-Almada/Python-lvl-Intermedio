# Python Package Manager

# pip es el gestor de paquetes de Python. Es una herramienta que permite buscar, instalar, actualizar y desinstalar paquetes o módulos de Python en nuestro sistema.

# Algunas cosas que se pueden hacer:
# pip install (para instalar dependencias)
# pip list (para ver la lista de librerías y dependencias que tengo instaladas)
# pip uninstall (para desinstalar una dependencia)
# pip show numpy (muestra información de la librería)

import numpy

print(numpy.version.version)

numpy_array = numpy.array([54,54,895,85,632,6898,3])
print(type(numpy_array))

print(numpy_array * 2)

import pandas
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(5, 4))
