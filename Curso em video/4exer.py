digito = input("Digite algo: ")

# Adicionando mais verificações e melhorando a saída
print('O tipo primitivo desse valor é:', type(digito))
print('Só tem espaços?', digito.isspace())
print('É um número?', digito.isnumeric())
print('É alfabético?', digito.isalpha())
print('É alfanumérico?', digito.isalnum())
print('Está em maiúsculas?', digito.isupper())
print('Está em minúsculas?', digito.islower())
print('Está capitalizada?', digito.istitle())



