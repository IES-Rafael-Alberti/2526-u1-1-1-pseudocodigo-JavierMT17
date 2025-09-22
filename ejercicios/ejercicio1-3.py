# Determinar si un número es primo
# Descripción: Indica si un número entero es primo (solo divisible entre 1 y él mismo).
# Entrada: Número entero X.
# Salida: Mensaje indicando si X es primo o no.

es_primo = True
numero = input("Introduzca un número: ")
numero = int(numero)

if numero < 2:
    es_primo = False

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False

if es_primo:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")

