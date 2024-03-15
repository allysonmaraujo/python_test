# listas
    # Armazenar mais de uma informação em variáveis
    # Manter a seqeuncia dos dados em uma variavel


#concatena atraves da variavel
letras = ['a', 'b', 'c', 'd']
numeros = [1, 2, 3, 4]
final = letras + numeros

print(final)


#concatena os indices das duas listas
cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]
duas_listas = zip(valores,cores)

print(list(duas_listas))