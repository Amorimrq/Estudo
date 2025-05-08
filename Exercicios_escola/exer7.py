soma = 0 

while True :
    number = int(input("Diga número inteiros que irei soma los (Um número negativo para parar): "))
    if number < 0 :
        break
    
    soma += number

print (f"A soma dos números são: {soma}")

