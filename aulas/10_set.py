
# Set (listas)

    # Similar a listas
    # Evita itens dupslicados
    # Nao utiliza index

list1 = [10, 20, 30 , 40, 50]
list2 = [10, 20, 30, 60, 70, 80]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)  # Union 
print(num1 - num2)  # Difference
print(num1 ^ num2)  # Assimetric Difference 
print(num1 & num2)  # And

print(len(num1))


# representação direta para set

set1 = {1, 2, 3, 4, 5}

# Mesmo adicionando itens duplicados, eles nao serao inclusos na set
set1.add(6)
set1.update([1, 2, 3, 7, 8,  9])

# remove: ocorre erro ao remover um item não existente
# discard: remove o item se tiver e senao tiver nao ocorre erro
set1.remove(7)
set1.discard(9)

print(set1)