

try:
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))

    multipiplicar = lambda x,y : x * y
    somar = lambda x,y : x + y
    subtrair = lambda x,y : x - y
    dividir = lambda x,y : x / y


    print(f'A soma de {numero1} com {numero2} é {somar(numero1, numero2)}')
    print(f'A multiplicação de {numero1} com {numero2} é {multipiplicar(numero1, numero2)}')
    print(f'A divisão de {numero1} com {numero2} é {dividir(numero1, numero2)}')
    print(f'A substração de {numero1} com {numero2} é {subtrair(numero1, numero2)}')
except ValueError:
    print('Apenas numeros inteiros são aceitos')