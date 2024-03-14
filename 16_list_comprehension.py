
    # List Comprehension

        # Mais simples de escrever
        # Utilizado quando você precisa criar uma nova lista a partir de uma existente
        # [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []




# exemplo normal 

for item in frutas1:
    if 'b' in item:
        frutas2.append(item)

print(frutas2)              # ['abacate', 'banana', 'abacaxi']




# List Comprehension

frutas3 = [iten for iten in frutas1 if 'n' in iten]
print(frutas3)               # ['banana', 'morango']