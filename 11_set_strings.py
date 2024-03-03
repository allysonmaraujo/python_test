
# Set (listas)

    # Similar a listas
    # Evita itens dupslicados
    # Nao utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)                 # {'d', 'b', 'c', 'e', 'a'}
set5 = set1.difference(set3)            # {'b', 'a'}
set6 = set1.intersection(set2)          # {'a'}
set7 = set1.symmetric_difference(set3)  # {'b', 'd', 'a', 'f'}

print(set7)