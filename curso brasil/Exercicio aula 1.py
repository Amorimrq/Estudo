#EXERCÍCIO: implemente o exemplo de switch case acima usando as condições "if/else"

#Prompt: para cada dígito entre 0-9, o programa imprimirá uma confirmação para o valor inserido 
# ou irá imprimir "invalid inputs" para todos os outros números.
number = input("Diga um number: ")

if number == '0':
    print("Entered 0")
elif number == '1':
    print("Entered 1")
elif number == '2':
    print("Entered 2")
elif number == '3':
    print("Entered 3")
elif number == '4':
    print("Entered 4")
elif number == '5':
    print("Entered 5")
elif number == '6':
    print("Entered 6")
elif number == '7':
    print("Entered 7")
elif number == '8':
    print("Entered 8")
elif number == '9':
    print("Entered 9")
else:
    print("Invalid number!")