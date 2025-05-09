print("TABUADA")

numeros = input("Digite os números separados por vírgula: ").split(",")
numeros = [int(numero.strip()) for numero in numeros]  # Converte os números para inteiros  e remove espaços extras
print("Você digitou:", numeros)     
for numero in numeros:
    print(f"Tabuada do {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
print("FIM DA TABUADA")


