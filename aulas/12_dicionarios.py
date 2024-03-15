

# Dicionarios

    # Utiliza index no formato de Keys e Values
    # Aceita String , Integer, Float, Boolean...


aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota_final' : 'A', 
    'aprovação': True,
    'materias': ['Fisica', 'Matematica', 'Portugues']
}

    # Não utiliza index, Ex: aluno[0]

    # utilizando Keys
print(aluno['nome'])


    # Atualizando itens
aluno['nome'] = 'Dayana'
    # OU
aluno.update({'nome': 'Maria', 'nota_final': 'B'})
aluno.update({'endereço': 'Rua A'})

    # pegando informação especificas do dicionarios
    # método  Get retorna uma informação caso ela nao exista
print(aluno.get('endereço'))
print(aluno.get('matricula', 'Essa informação não existe'))

    # For para impressão de valores ou propriedades
for x in aluno.keys():
    print(x)

for y in aluno.values():
    print(y)

for w in aluno.items():
    print(w)

print(aluno.get('materias'))
    # tamanho da lista
print(len(aluno))