idade = int(input("Diga sua idade: "))

if idade >= 18 and idade < 60:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Menor de idade")
