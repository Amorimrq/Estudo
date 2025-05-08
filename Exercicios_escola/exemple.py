#Escreva um programa que peça ao usuário dois números. ]
# Verifique se o primeiro número é positivo. Se for, verifique se o segundo número também é positivo.
#  Se ambos forem positivos, exiba Ambos os números são positivos". 
# Caso contrário, não exiba nada.
number = int(input("Diga um número: "))
number2 = int(input("Diga outro número: "))

if number and number2 > 0 : 
        print("Ambos os números são positivos")
else :
    print("")