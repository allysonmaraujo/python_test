# listas
    # Armazenar mais de uma informação em variáveis
    # Manter a seqeuncia dos dados em uma variavel

cidade1 = 'Rio de Janeiro'
cidade2 = 'Sao Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'Sao Paulo', 'Salvador', 'Goiania']

cidades.append('Florianopolis') # adiciona ao final da lista
cidades.remove('Salvador')      # remove de acordo com que é inserido
cidades.insert(1, 'Belem')      # insere no indice e o valor
cidades.pop(0)                  # remove de acordo com o indice
cidades.sort()                  # organiza por ordem alfabética ou numerica

#forma cada letra e espaço como indice em uma array
var = list(cidade1)
print(var)

#criar um array a partir de um imput feito pelo usuario
frutas_usuario = input('Digite o nome das frutaws separadas por virgulas e com espaço: ')
frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)