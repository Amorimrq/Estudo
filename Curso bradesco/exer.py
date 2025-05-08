def notas():
    n1 = float(input('Digite uma nota: '))
    return n1

def media(n1,n2):
    m = (n1 + n2) / 2
    print(f'Nota 1: {n1}')
    print(f'Nota 2: {n2}')
    if m >= 7:
        print(f'Média: {m} - Aprovado')
    elif m >= 5:
        print(f'Média: {m} - Recuperação')
    else:
        print(f'Média: {m} - Reprovado')

a = notas()
b = notas()
media(a, b)

