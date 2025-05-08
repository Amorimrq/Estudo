soma = 0 
while True :
    n = int(input("Diga numeros: "))
    soma = n + soma 
    if n < 0 :
        break
print(soma)