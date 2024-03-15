from datetime import datetime

try:
    ano_nascimento = int(input('Coloque o ano em que nasceu com 4 digitos: '))
    idade = datetime.now().year - ano_nascimento

    if ano_nascimento > datetime.now().year:
        print('Ano invalido')
    if idade in range (1,17):
        print('Menor de idade')
    elif idade > 18:
        print('Maior de idade')

except ValueError:
    print('Aceito apenas numeros inteiros')

