from math import sqrt
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
h = sqrt(co**2 + ca**2)
print(f'AS somas do catetos {co} e {ca} é {h:.3f}')
