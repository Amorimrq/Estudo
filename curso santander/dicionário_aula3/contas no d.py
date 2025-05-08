frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), 
# a diferença (-) e a diferença simétrica (^).
união = conjunto1 | conjunto2
print(união)

intersecao = conjunto1 & conjunto2
print(intersecao)

diferença = conjunto1 - conjunto2
print(diferença)

simetrica = conjunto1 ^ conjunto2 
print (simetrica)