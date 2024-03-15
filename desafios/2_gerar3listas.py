# Criar um programa que gera 3 listas de acordo com a necessidade abaixo:

# lista1 = Funcionarios que trabalham de carro e a noite
# lista2 = Funcionarios que trabalham de carro e de dia
# lista3 = Funcionarios que nao tem carro

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
lista2 = set(tem_carro).intersection(turno_dia)
lista3 = set(funcionarios).difference(tem_carro)

print(lista1) # {'Bruno'}
print(lista2) # {'Melissa', 'Alice', 'Marcos'}
print(lista3) # {'Sophia', 'Ana', 'Pedro'}