
# Map Function

    # Muito utilizda com listas
    # Aplicar uma função a um Interable por item (list, tuple, dic, etc)

lista1 = [1, 2, 3, 4]

def mullt(x):
    return x * 200
lista2 = map(mullt, lista1)
print(list(lista2)) # [200, 400, 600, 800]

lista3 = map(lambda x: x * 200, lista1)
print(list(lista3)) # [200, 400, 600, 800]