#2. Par ou Ímpar* Crie um programa que solicite um número ao usuário e informe se ele é par ou ímpar. 
number = int(input("Diga um Número: "))
if number % 2:
    print(f"O Número {number} é Impar")
else :
    print(f"O Número {number} é Par")