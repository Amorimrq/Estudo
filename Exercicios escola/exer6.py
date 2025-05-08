#6. Nota e Conceito* Faça um programa que receba uma nota de 0 a 10 e classifique-a 7
# conforme a seguinte tabela: A se a nota for 9 ou 10 B se for 7 ou 8 C se for 5 ou 6 D se for 3 ou 4 F se for menor que 3.
nota = int(input('Diga sua nota'))

if nota >= 9 :
    print("A")
elif nota == 7 or nota == 8:
    print("B")
elif nota == 5 or nota == 6:
    print("C")
elif nota == 3 or nota == 4:
    print("D")
elif nota <= 2:
    print("F")
    