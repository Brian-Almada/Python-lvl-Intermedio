# Challenges

"""
"FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluídos y con un salto de línea entre cada impresión) sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""
"""
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        else:
            i = "FizzBuzz"  <-- Aquí al dejarlo en else va a tomar cualquier número por el cual no se cumpla. Esta condición debería ser el primer if del código ya que es la condición más restrictiva
        print(i)

fizzbuzz()
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        print(i)

fizzbuzz()

"""
Escribe una función que reciba dos palabras (String) y retorne True o False según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_an_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_an_anagram("amor", "goma"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos    anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def suc_fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

suc_fibonacci()


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es primo o no.
Hecho esto imprime los números primos del 1 al 100
"""



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(1, 101):
    if is_prime(num):
        primes.append(num)

print("Los números primos del 1 al 100 son:", primes)


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers = list(range(1, 101))
for num in numbers:
    if is_prime(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")




