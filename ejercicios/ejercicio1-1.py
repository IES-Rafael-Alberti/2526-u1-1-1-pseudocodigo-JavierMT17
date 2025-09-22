# Determinar si un número es par o impar
# Descripción: Programa que pide un número entero y determina si es par (divisible entre 2) o impar.
# Entrada: Número entero X.
# Salida: Mensaje indicando si X es par o impar.

numero = input("Introduzca un número: ")
numero = int(numero)

if numero % 2 == 0:
    print(numero,"es par")
else:
    print(numero,"es impar")

