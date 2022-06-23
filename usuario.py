from block import AlteracoesBlockchain
from banco import ManipularBancos

blockchain = AlteracoesBlockchain()
bancos = ManipularBancos()

class OpcoesUsuario:

    def __init__(self):
        pass

    def pegar_dados_conexoes(self):

        #RECEBE DADOS DE CONEXÃO COM O BANCO A SER INSERIDO

        driver_banco = "MySQL ODBC 8.0 ANSI Driver;"
        server = "localhost;"
        database = "blocktest;"
        tabela = "historico_hash"
        user = "root"
        password = ""

        #PASSA OS DADOS DE CONEXÃO DO USUÁRIO
        bancos.armazenar_login_temporario(driver_banco,server,database,tabela,user,password)

        #TESTA PARA VER SE ALGO DEU ERRADO PARA EVITAR FALHAS DE CONEXÃO AO LOGO DO PROCESSO
        bancos.conectar_banco_imutavel()

def iniciar_projeto(conteudo):
    OpcoesUsuario().pegar_dados_conexoes()
    blockchain.novo_bloco(conteudo)

"""

Traduzir
Apresentar arquitetura(Geral -> C# -> Api -> Server -> Block) e estrutura(Interno/ Classes relacionadas)

"""
