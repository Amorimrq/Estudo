#Escreva um programa que peça uma senha ao usuário. Se a senha for "admin", peça uma segunda verificação para confirmar a senha. 
# Se a confirmação também for "admin", 
# exiba "Acesso permitido". Caso contrário, exiba "Senha incorreta".
senha = input("Qual a senha: ")

if senha == 'admin' :
    n = input("Reconfime a senha: ")
    if n == 'admin' :
        print ("Acesso liberado")
    else :
        print ("Acesso negado")
else :
    print ("Acesso negado")