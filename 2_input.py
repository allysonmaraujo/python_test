# o André tem 28 anos de idade e mora na cidade de São Paulo

nome = str(input('Digite um nome: '))
idade = int(input('Digite a sua idade: '))
try:
  idade = int(idade)
except ValueError:
  print('Digite apenas números inteiros')
cidade = str(input('Digite a cidade onde mora: '))

print(f' {nome} tem {idade} anos de idade e mora na cidade de {cidade}')
print(nome + ' tem ' + str(idade) + ' anos de idade e mora na cidade de '+ cidade)