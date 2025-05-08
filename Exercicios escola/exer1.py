# Verificação Simples* Escreva um programa que solicite ao usuário um número inteiro e exiba a mensagem "Positivo" 
# se o número for maior que zero. 
number = int(input("Diga um número: "))
if number > 0:
    print(f"O Número {number} é Positivo")
else:
    print(f"O número {number} é Negativo")