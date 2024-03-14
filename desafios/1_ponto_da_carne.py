
try:
    temperatura = int(input('Digitar o(s) numero(s) da temperatura de carne em Celsius : '))

    if temperatura < 47:
        print('Precisa de mais tempo para assar!')
    if temperatura in range(48,53):
        print('Selada')
    if temperatura in range(54,59):
        print('Ao Ponto para mal passada')
    if temperatura in range(60,64):
        print('Ao ponto')
    if temperatura in range(65,70):
        print('Ao ponto para bem passada')
    if temperatura >= 71:
        print('Bem passada')
except ValueError:
    print('Apenas numeros inteiros são válidos')


