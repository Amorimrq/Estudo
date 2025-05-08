import random
from time import sleep
print('Jogo da velha')
escolhas = ['tesoura', 'papel', 'pedra']
def vencedor(usuario, computador):
    if usuario == computador:
        return 'Empate'
    elif (usuario == 'tesoura' and computador == 'pedra' ) or\
        (usuario == 'papel' and computador == 'tesoura') or\
        (usuario == 'pedra' and computador == 'papel'):
        return 'O Computador Venceu'
    else :
        return 'O Usuário Venceu'
sleep(1)
usuario = input("Qual sua escolha: ").lower()
if usuario not in escolhas:
    print("Opção invalida")
else:
    sleep(1)
    computador = random.choice(escolhas)
    print(f'O computador escolheu {computador}')
    sleep(1)
    print(f"O Usuário escolheu {usuario}")
    resultado = vencedor(usuario, computador)
    sleep(1)
    print(resultado)