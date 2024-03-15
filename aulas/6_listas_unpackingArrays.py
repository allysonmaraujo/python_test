# listas
    # Armazenar mais de uma informação em variáveis
    # Manter a seqeuncia dos dados em uma variavel


produtos = ['banana', 'feijao', 'laranja', 'arroz', 1, 2, 3, 4, 'tomate']

item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]

#ou

item1, item2, item3, item4, *numeros, item5 = produtos


print(item1)
print(item2)
print(item3)
print(item4)
print(numeros)
print(item5)