# Dates

from datetime import datetime

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

