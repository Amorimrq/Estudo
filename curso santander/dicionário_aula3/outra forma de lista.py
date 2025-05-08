frutas = {"maça", 'banana', 'uva'}
print(frutas)

frutas.add ("pera")
print(frutas)

frutas.remove ('banana')
print(frutas)

#discard: remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
frutas.discard ('uva')
print(frutas)

frutas.discard('abacaxi')
print(frutas)

frutas.clear()
print(frutas)