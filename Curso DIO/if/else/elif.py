saldo = 1000
saque = 1300
bonus = 500
if saldo >= saque:
    print("Realizando saque")
else:
    print("Saldo insufuciente")

if saldo >= saque:
    print("Realizando saque")
elif saque>= (saldo + bonus):
    print("Realizando saque com bonus")
else:
    print("Saldo insuficiente")

print("realizado") if saldo >= saque else print("ERRo")