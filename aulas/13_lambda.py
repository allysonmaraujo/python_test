

# Lambda Function
    # Uma funcção pequena sem nome
    # Pode ter varios argumentos mas somente uma expressao
    # Muito utilizada dentro de outras funções
    # Codigo mais clean

    # Função comum
def somar(x):
    return x + 10

    # Função lambda
somar1n = lambda x : x + 10 
somar2n = lambda x,y : x + y + 20

print(somar(2))         # 12
print(somar1n(2))       # 12 
print(somar2n(10,20))   # 50


#Função Lambda dentro de outra função

def somar2x(x):
    somar1 = lambda x: x + 5
    return somar1(x) + x

print(somar2x(10))      # 25