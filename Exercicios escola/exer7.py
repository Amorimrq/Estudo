#7. Login Simples* Crie um programa que peça um nome de usuário e uma senha. Caso o usuário digite "admin" como nome 
# e "1234" como senha, exiba "Login bem-sucedido". Caso contrário, exiba "Usuário ou senha incorretos". 
nom = 'admin'
sen = 1234
nome = input("Diga seu nome: ")
senha = int(input("Diga a senha: "))

if nome == nom and senha == sen:
    print("Login Bem-Sucedido")
else:
    print('Usuário ou senha incorreto')

