number1 = int(input("nÚMERO: "))
number2 = int(input("numero: "))
soma = number1 / number2
#


try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
    