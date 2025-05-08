lista = set()
quer_continuar = str('sim')
while True:
   lista.add (input("Insira do dado: "))
   print(lista)
   n = input("Quer continuar [1] Sim [2] Não: ")
   if n == "1":
      continue
   if n == "2":
      break
print (lista)