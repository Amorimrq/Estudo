#4. Triângulo Válido* Desenvolva um programa que receba três números inteiros representando os lados de um triângulo. 

# O programa deve verificar se a soma de dois lados é sempre maior que o terceiro e informar se os valores formam um triângulo válido. 
print("Vamos descobrir se é um triangulo")
print("Considerando 'C' a base e 'A' e 'B' os lados")
n1, n2, n3 = map(int, input("Diga os Valores de A B e C respectivamente(exemp:2 5 3): ").split())

if n1 + n2 > n3:
    print("Triangulo Valido")
else:
    print("Triangulo Invalido")
    


