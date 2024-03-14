# Filter Function

    # Muito utilizada em listas
    # Aplicar uma função a um Iterabe, filtrando itens (list, tuple, dic, etc)

valores = [10, 20, 30, 40, 50]

def remover20(x):
    return x > 20

print(list(map(remover20, valores)))                # [False, False, True, True, True]

print(list(filter(remover20, valores)))             # [30, 40, 50]
print(list(filter(lambda x: x > 20, valores)))      # [30, 40, 50]