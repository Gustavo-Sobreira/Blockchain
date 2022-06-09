from blockchain import Blockchain
from bancosql import Banco_SQL
from random import randint




block = Blockchain()
banco = Banco_SQL()

#Mudar os nomes Aqui
block.novo_bloco(banco.manipular_banco(f"NomeTabela"))

