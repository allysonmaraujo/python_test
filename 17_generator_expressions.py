from sys import getsizeof

# Generator Expressions

    # Uma forma mais rapida para listas, dicionarios, etc
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(1000000)]
print(type(numeros))        # <class 'list'>
print(getsizeof(numeros))   # 8448728 (Tamanho de memória alocada)

# Generator Expressions ficam em parenteses 
numeros = (x * 10 for x in range(1000000))
print(type(numeros))        # <class 'generator'>
print(getsizeof(numeros))   # 104 (Tamanho de memória alocada)



