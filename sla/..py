import random
from time import sleep

l = input('Diga seu nome: ')
lista_golpes1 = ['Super Soco', 'Kamekame HAAA', 'Vazio Roxo']
hp1 = 200

l2 = input("Diga nome do outro lutador: ")
lista_golpes2 = ['DETROID SMASH', 'CHUTE STYLE', 'Genki Dama']
hp2 = 200

print('1')
sleep(1)
print("2")
sleep(1)
print('3')
sleep(1)
print("LUTEM")

while hp1 > 0 and hp2 > 0:
    # Escolhe um golpe aleatório para o lutador 1
    golpe = random.choice(lista_golpes1)
    dano = random.randint(1, 40)
    hp2 -= dano
    sleep(1)
    print(f'O {l} deu um {golpe} em {l2} (Vida {hp2})')

    if hp2 <= 0:
        print(f'{l2} foi derrotado!')
        break
    
    # Escolhe um golpe aleatório para o lutador 2
    golpe2 = random.choice(lista_golpes2)
    dano2 = random.randint(1, 40)
    hp1 -= dano2
    sleep(1)
    print(f'O {l2} deu um {golpe2} em {l} (Vida {hp1})')

    if hp1 <= 0:
        print(f'{l} foi derrotado!')
        break
