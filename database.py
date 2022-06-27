import pyodbc

class Manipulate_database:

    def __init__(self):
        pass

    def connect_immutable_database(self):

        # DADOS DE LOCALIZAÇÃO DA BLOCKCHAIN NO BANCO
        database_driver = "MySQL ODBC 8.0 ANSI Driver;"
        server = "localhost;"
        database = "blocktest;"
        user = "root"
        password = ""

        #FAZ CONEXÃO COM O BANCO QUE OS ARQUIVOS SERÃO ESCRITOS
        print("     -----   CONECTANDO A BLOCKCHAIN   -----")
        try:
            connection = pyodbc.connect(f"""DRIVER={database_driver};SERVER={server};DATABASE={database};UID={user};PWD={password}""")
        except Exception:
            print("        ERRO NA CONEXÃO COM A BLOCKCHAIN")
            exit()

        else:
            print("       CONECTADO A BLOCKCHAIN COM SUCESSO")
            return connection

        finally:
            print("     ---------------------------------------")

    def get_last_hash(self):
        table = "historico_hash"

        #FAZ PEDIDO DE CONEXÃO
        cursor = self.connect_immutable_database().cursor()
        # FAZ A SEARCH NO Banco DE FORMA QUE O ULTIMO ID SEJA SELECIONADO 1°

        #SQL search = f"""SELECT [Current_hash] FROM [dbo].[{Manipulate_database.databaseaida[3]}] ORDER BY ID DESC"""
        search = f"""SELECT HASH_ATUAL FROM {table} ORDER BY ID DESC"""

        cursor.execute(search)
        row = cursor.fetchall()

        #TRAZ APENAS O MAIOR ID
        global last_hash
        for last_hash in row:
            last_hash = last_hash[0]
            break

        if row == []:
            last_hash = 0

        return last_hash


    def record_blockchain_data(self,last_hash,current_hash,nonce,content):
        table = "historico_hash"

        #FAZ PEDIDO DE CONEXÃO
        cursor = self.connect_immutable_database().cursor()

        #SQL insert = f"""INSERT INTO [dbo].[{Manipulate_database.databaseaida[3]}](Last_hash,Current_hash,Nonce,Content)
        #VALUES('{last_hash}','{current_hash}','{nonce}','{content}');"""

        insert = f"""INSERT INTO {table}(HASH_ANTERIOR,HASH_ATUAL,NONCE,ACAO)
                VALUES('{last_hash}','{current_hash}','{nonce}','{content}');"""

        cursor.execute(insert)

        #INSERT OS DADOS NA BLOCKCAHIN
        cursor.commit()
        cursor.close()
