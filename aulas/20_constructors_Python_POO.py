# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar

    # Class: Frutas
    # Objects: Abacate, Banana...

from datetime import datetime

#Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        return datetime.now().year - self.ano_nascimento



#Criar o objeto
usuario1 = Funcionarios('Elena','Cabral', 1982)
usuario2 = Funcionarios('Carol', 'Melo', 2003)

#print
print(usuario1.ano_nascimento) # 12/09/1982
print(usuario2.ano_nascimento) # 23/03/2003

print(usuario1.nome_completo())             # Elena Cabral
# ou
print(Funcionarios.nome_completo(usuario1)) # Elena Cabral
print(Funcionarios.idade_funcionario(usuario1)) # 42
print(Funcionarios.idade_funcionario(usuario2)) # 21