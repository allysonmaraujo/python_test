try:
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))
    numero3 = int(input('Digite o terceiro numero: '))
    numero4 = int(input('Digite o quarto numero: '))
    numero5 = int(input('Digite o quinto numero: '))

    lista = [numero1, numero2, numero3, numero4, numero5]
    quadrado = []

    for numero in lista:
        # resultado = lambda num : num**2
        quadrado.append(numero**2)

    print(f'os valores quadrados para a lista {lista} serão {quadrado}')
except ValueError:
    print('Aceito apenas numeros inteiros')