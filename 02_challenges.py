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