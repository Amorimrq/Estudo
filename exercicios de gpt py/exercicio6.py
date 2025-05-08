numeros = []

for i in range (5) :
    numero = int(input(f"Digite {i + 1}º o numero inteiro"))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(maior)
print (menor)

