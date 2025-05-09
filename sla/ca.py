CONTA_VALIDA = "000323"
SENHA_VALIDA = "9883"
SALDO_INICIAL = 1500.00

def realizar_saque(saldo):
    while True:
        try:
            valor_saque = int(input("Informe o valor para saque: R$ "))
            if valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor_saque % 10 != 0:
                print("O valor deve ser múltiplo de 10 para ser sacado com as notas disponíveis.")
            else:
                notas = [100, 50, 20, 10]
                quantidade_notas = {}
                for nota in notas:
                    quantidade_notas[nota], valor_saque = divmod(valor_saque, nota)
                print("Notas entregues:")
                for nota, quantidade in quantidade_notas.items():
                    if quantidade > 0:
                        print(f"{quantidade} nota(s) de R$ {nota}")
                saldo -= sum(nota * quantidade for nota, quantidade in quantidade_notas.items())
                print(f"Novo saldo: R$ {saldo:.2f}")
                break
        except ValueError:
            print("Por favor, insira um valor válido.")
    return saldo

def main():
    print("Bem-vindo ao Caixa Eletrônico!")
    conta = input("Digite o número da conta: ")
    senha = input("Digite a senha: ")

    if conta == CONTA_VALIDA and senha == SENHA_VALIDA:
        saldo = SALDO_INICIAL
        print(f"Login bem-sucedido! Saldo disponível: R$ {saldo:.2f}")
        while True:
            saldo = realizar_saque(saldo)
            opcao = input("Deseja realizar outro saque? (s/n): ").strip().lower()
            if opcao != 's':
                print("Obrigado por utilizar o Caixa Eletrônico. Até logo!")
                break
    else:
        print("Conta ou senha inválida. Encerrando o programa.")

if __name__ == "__main__":
    main()