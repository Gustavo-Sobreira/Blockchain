import pyodbc

class ManipularBancos:


    bancoEntrada = []
    bancoSaida = []
    login = []

    def __init__(self):
        pass

    def armazenar_login_temporario(self,banco_entrada,servidor_entrada,nome_entrada,tabela_entrada,banco_saida,servidor_saida,nome_saida,tabela_saida,usuario,senha):

        #DE ONDE OS DADOS SERÃO PEGOS
        ManipularBancos.bancoEntrada.append(banco_entrada)
        ManipularBancos.bancoEntrada.append(servidor_entrada)
        ManipularBancos.bancoEntrada.append(nome_entrada)
        ManipularBancos.bancoEntrada.append(tabela_entrada)

        #PARA ONDE OS DADOS VÃO
        ManipularBancos.bancoSaida.append(banco_saida)
        ManipularBancos.bancoSaida.append(servidor_saida)
        ManipularBancos.bancoSaida.append(nome_saida)
        ManipularBancos.bancoSaida.append(tabela_saida)

        #USUÁRIO E SENHAS DEVEM SER IGUAIS, NOS DOIS BANCOS
        ManipularBancos.login.append(usuario)
        ManipularBancos.login.append(senha)


    def conectar_banco_entrada(self):

        #FAZ CONEXÃO COM O BANCO QUE OS ARQUIVOS SERÃO RETIRADOS
        conexao = pyodbc.connect(f"""DRIVER={ManipularBancos.bancoEntrada[0]};SERVER={ManipularBancos.bancoEntrada[1]};DATABASE={ManipularBancos.bancoEntrada[2]};UID={ManipularBancos.login[0]};PWD={ManipularBancos.login[1]}""")

        return conexao


    def conectar_banco_saida(self):

        #FAZ CONEXÃO COM O BANCO EM QUE SERÁ GRAVADA A BLOCKCHAIN
        conexao = pyodbc.connect(f"""DRIVER={ManipularBancos.bancoSaida[0]};SERVER={ManipularBancos.bancoSaida[1]};DATABASE={ManipularBancos.bancoSaida[2]};UID={ManipularBancos.login[0]};PWD={ManipularBancos.login[1]}""")

        return conexao


    def verificar_conexoes(self):
        self.conectar_banco_entrada()
        self.conectar_banco_saida()


    def extrair_conteudo_entrada(self):
    #Desnecessário por enquanto
        #FAZ PEDIDO DE CONEXÃO
        cursor = self.conectar_banco_entrada().cursor()

        #FAZ A BUSCA NO SQL DE FORMA QUE O ULTIMO ID SEJA SELECIONADO 1°
        busca = f"""SELECT * FROM {ManipularBancos.bancoEntrada[3]} ORDER BY ID DESC"""
        cursor.execute(busca)
        linhas = cursor.fetchall()

        #TRAZ APENAS O MAIOR ID
        global conteudo_entrada
        for conteudo_entrada in linhas:
            conteudo_entrada = linhas[0]
            break


#Descobrir comoo retirar as aspas do conteudo




        conteudo_entrada ="""(1, 123, 123.0, 1123, asd, asd, 123, 123.0, asd, 123, 123, asdasd, asddas)"""
        return conteudo_entrada


    def pegar_ultimo_hash(self):

        #FAZ PEDIDO DE CONEXÃO
        cursor = self.conectar_banco_saida().cursor()
        # FAZ A BUSCA NO SQL DE FORMA QUE O ULTIMO ID SEJA SELECIONADO 1°
        #SQL busca = f"""SELECT [Hash_atual] FROM [dbo].[{ManipularBancos.bancoSaida[3]}] ORDER BY ID DESC"""
        busca = f"""SELECT Hash_atual FROM {ManipularBancos.bancoSaida[3]} ORDER BY ID DESC"""
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
        cursor = self.conectar_banco_saida().cursor()
        #SQL insere = f"""INSERT INTO [dbo].[{ManipularBancos.bancoSaida[3]}](Hash_anterior,Hash_atual,Nonce,Conteudo)
        #VALUES('{hash_anterior}','{hash_atual}','{nonce}','{conteudo}');"""
        insere = f"""INSERT INTO {ManipularBancos.bancoSaida[3]}(Hash_anterior,Hash_atual,Nonce,Acao)
                VALUES("{hash_anterior}","{hash_atual}","{nonce}","{conteudo}");"""

        cursor.execute(insere)
        #INSERE OS DADOS NA BLOCKCAHIN
        cursor.commit()
        cursor.close()
