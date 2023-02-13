# Dates

from datetime import datetime # El módulo datetime proporciona clases para manipular fechas y horas. Si bien la implementación permite operaciones aritméticas con fechas y horas, su principal objetivo es poder extraer campos de forma eficiente para su posterior manipulación o formateo.

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(now)

timestamp = now.timestamp() # Se toma como medida de tiempo el número de segundos transcurridos desde el primero de enero de 1970 a las 0 horas UTC hasta el momento a representar

print(timestamp)

year_2023 = datetime(2023, 1, 22)

print_date(year_2023)

from datetime import time

print(time)

current_time = time(11, 20, 30) # Time es un objeto que tiene las propiedades de tiempo (horas, minutos y segundos). Pero estos están vacíos y nos toca rellenarlos con valores que necesitemos. Si no pasamos parámetros, los print siguientes tendran un valor de 0

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

print(date)

current_date = date(2023, 2, 13) # Date es similar a Time, la diferencia es que date tiene las propiedades de las fechas. También debemos rellenar con valores, pero no se puede instanciar sin valor ya que no nos devuelve 0 como time, sino que nos devuelve la excepción TypeError

print(current_date.year)
print(current_date.month)
print(current_date.day)

