# Generar la tabla de multiplicar de un número
# Descripción: Genera la tabla de multiplicar del número introducido, desde 1 hasta 10.
# Entrada: Número entero X.
# Salida: Series de líneas “X x i = resultado”.

numero = input("Introduce un número: ")
numero = int(numero)
for multiplo in range(1, 11):
    print(f"{numero} x {multiplo} = {numero * multiplo}")

