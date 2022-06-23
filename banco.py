import pyodbc

class ManipularBancos:

    banco_imutavel = []

    def __init__(self):
        pass

    def armazenar_login_temporario(self,driver,server,database,tabela,user,password):

        #CONEXÃO ONDE OS DADOS SERÃO ALOCADOS

        ManipularBancos.banco_imutavel.append(driver)
        ManipularBancos.banco_imutavel.append(server)
        ManipularBancos.banco_imutavel.append(database)
        ManipularBancos.banco_imutavel.append(tabela)
        ManipularBancos.banco_imutavel.append(user)
        ManipularBancos.banco_imutavel.append(password)

    def conectar_banco_imutavel(self):

        #FAZ CONEXÃO COM O BANCO QUE OS ARQUIVOS SERÃO RETIRADOS
        conexao = pyodbc.connect(f"""DRIVER={ManipularBancos.banco_imutavel[0]};SERVER={ManipularBancos.banco_imutavel[1]};DATABASE={ManipularBancos.banco_imutavel[2]};UID={ManipularBancos.banco_imutavel[4]};PWD={ManipularBancos.banco_imutavel[5]}""")
        return conexao

    def pegar_ultimo_hash(self):

        #FAZ PEDIDO DE CONEXÃO
        cursor = self.conectar_banco_imutavel().cursor()
        # FAZ A BUSCA NO Banco DE FORMA QUE O ULTIMO ID SEJA SELECIONADO 1°

        #SQL busca = f"""SELECT [Hash_atual] FROM [dbo].[{ManipularBancos.bancoSaida[3]}] ORDER BY ID DESC"""
        busca = f"""SELECT Hash_atual FROM {ManipularBancos.banco_imutavel[3]} ORDER BY ID DESC"""

        cursor.execute(busca)
        linhas = cursor.fetchall()

        #TRAZ APENAS O MAIOR ID
        global hash_anterior
        for hash_anterior in linhas:
            hash_anterior = hash_anterior[0]
            break

        if linhas == []:
            hash_anterior = 0

        return hash_anterior


    def gravar_dado_blockchain(self,hash_anterior,hash_atual,nonce,conteudo):

        #FAZ PEDIDO DE CONEXÃO
        cursor = self.conectar_banco_imutavel().cursor()

        #SQL insere = f"""INSERT INTO [dbo].[{ManipularBancos.bancoSaida[3]}](Hash_anterior,Hash_atual,Nonce,Conteudo)
        #VALUES('{hash_anterior}','{hash_atual}','{nonce}','{conteudo}');"""

        insere = f"""INSERT INTO {ManipularBancos.banco_imutavel[3]}(Hash_anterior,Hash_atual,Nonce,Acao)
                VALUES("{hash_anterior}","{hash_atual}","{nonce}","{conteudo}");"""

        cursor.execute(insere)

        #INSERE OS DADOS NA BLOCKCAHIN
        cursor.commit()
        cursor.close()
