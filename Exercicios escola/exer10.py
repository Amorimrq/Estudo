#Digite o número da conta: 000323
#Digite a senha: 9883
#Saldo disponível: R$1000.00
#Digite o valor que deseja sacar: R$530
#Saque realizado com sucesso!
#Notas de R$100: 5x
#Notas de R$20: 1x
#Notas de R$10: 1x
#Deseja realizar outro saque? (s/n): não
#Atendimento encerrado. Até logo!r 
# o atendimento.
conta = '000323'
senha = '9883'
saldo = float(1000)

usuario = input("Seu nome de usuario: ")
senha_senha = input("Qual a sua senha: ")
if usuario == conta and senha_senha == senha:
    print("Login bem sucedido0")
else:
    print("erro")
print(f"Seu saldo é {saldo}")
continuar = int(input("Quer realizar um saque?: "))
if continuar == 'sim':
    notas = [100, 50, 20, 10]
    entregues = {100: 0, 50:0, 20:0, 10:0}
    valor_restante = 0
    for nota in notas:
        print("não sei fazer")
SystemError