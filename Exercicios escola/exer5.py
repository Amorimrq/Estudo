#5. Maior de Três Números* Escreva um programa que solicite três números ao usuário e exiba qual deles é o maior. 
print("Qual o maior número?")
n1, n2, n3 = map(int,input("Diga Três Número: ").split())
numero = max(n1, n2, n3)
print(f'O  maior número é {numero}')