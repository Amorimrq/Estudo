#8. Ano Bissexto* Elabore um programa que solicite um ano ao usuário e determine se ele é bissexto ou não. 
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400. 

ano = int(input("Diga um ano: "))
if (ano % 4 == 0 and ano %100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é Bissexto")
else:
    print(f"O ano {ano} não bissexto") 