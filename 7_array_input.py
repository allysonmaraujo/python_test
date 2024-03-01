# listas
    # Armazenar mais de uma informação em variáveis
    # Manter a seqeuncia dos dados em uma variavel


cores_cliente = input('Digite uma cor para verificar o estoque: ')
cores = ['amarelo', 'verde', 'vermelho', 'roxo']

#faz uma varredura da array com todas as letras em minusculas (lowerCase)
if cores_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não tem em estoque')

