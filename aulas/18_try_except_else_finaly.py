

    # Erros

        # Excelentes para testes
        # Nao realiza stop no programa
        # Mensagens customizadas


# EXCEPT
try:   #index  0    1    2
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index nao existe')


# ELSE executa CASO ocorra não ocorra erro
    try:
        valor = int(input('Digite o valor do seu produto: '))
        print(valor)
    except ValueError:
        print('Apenas numeros inteiros são validos') 
    else:
        print('Usuario digitou o numero correto')
        resultado = valor * 30
        print(resultado)

# FINALY executa mesmo com erros no caminho do código
    try:
        valor = int(input('Digite o valor do seu produto: '))
        print(valor)
    except ValueError:
        print('Apenas numeros inteiros são validos') 
    finally:
        print('Codigo Ok')



print('continuação do código')