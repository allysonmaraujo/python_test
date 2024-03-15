import arquivo_de_teste
arquivo_de_teste.soma()
arquivo_de_teste.mult()


# ou
from arquivo_de_teste import soma, mult
soma()
mult()

# necessario colocar dentro da pasta um arquivo __init__.py para identificar como package
from itens.arquivos_de_testes import sub, div
sub()
div()