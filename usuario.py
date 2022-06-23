from block import AlteracoesBlockchain
from banco import ManipularBancos
import app

blockchain = AlteracoesBlockchain()
bancos = ManipularBancos()


class OpcoesUsuario:

    def __init__(self):
        pass

    def pegar_dados_conexoes(self):

        #PASSA DADOS DE CONEXÃO COM O BANCO QUE OS ARQUIVOS SERÃO RETIRADOS
        banco_entrada = "MySQL ODBC 8.0 ANSI Driver;"
        servidor_entrada = "localhost;"
        nome_entrada = "blocktest"
        tabela_entrada = "historico_hash"

        #PASSA DADOS DE CONEXÃO COM O BANCO EM QUE SERÁ GRAVADA A BLOCKCHAIN
        banco_saida = "MySQL ODBC 8.0 ANSI Driver;"
        servidor_saida = "localhost"
        nome_saida = "blocktest"
        tabela_saida = "historico_hash"

        #PESSSOA NÃO PODE ALTERAR SUA SENHA NEM USUÁRIO
        usuario = "root"
        senha = ""

        #PASSA OS DADOS DE CONEXÃO DO USUÁRIO E SEUS BANCOS DE ENTRADA E SAIDA
        bancos.armazenar_login_temporario(banco_entrada,servidor_entrada,nome_entrada,tabela_entrada,banco_saida,servidor_saida,nome_saida,tabela_saida,usuario,senha)

        #TESTA PARA VER SE ALGO DEU ERRADO PARA EVITAR FALHAS DE CONEXÃO AO LOGO DO PROCESSO
        bancos.verificar_conexoes()

        print("="*95)
        print("""
                                BANCOS CONECTADOS COM SUCESSO
                                  CRIPTOGRAFIA EM ANDAMENTO     
                     """)
        print("=" * 95)


    def iniciar_blockchain(self,conteudo):

        continuar = 0
        while (continuar != 1) and (continuar != 3):
            continuar = int(input("""
    ESCOLHA ENTRE AS SEGUINTES OPÇÕES:
    
    [ 1 ] -> CRIPTOGRAFAR NOVOS DADOS
    [ 3 ] -> ENTERROMPER O SISTEMA
    
    DIGA SUA ESCOLHA: """))
        print("")
        print("=" * 95)

        if continuar == 1:
            #conteudo = bancos.extrair_conteudo_entrada()
            blockchain.novo_bloco(conteudo)
            usuario.iniciar_blockchain()

        else:
            exit()

usuario = OpcoesUsuario()

def iniciar_projeto(conteudo):
    usuario.pegar_dados_conexoes()
    blockchain.novo_bloco(conteudo)
    #usuario.iniciar_blockchain(conteudo)



"""

Limpar código
Traduzir
Apresentar arquitetura(Geral -> C# -> Api -> Server -> Block) e estrutura(Interno/ Classes relacionadas)

"""