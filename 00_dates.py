# Dates

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp() # Se toma como medida de tiempo el número de segundos transcurridos desde el primero de enero de 1970 a las 0 horas UTC hasta el momento a representar

print(timestamp)