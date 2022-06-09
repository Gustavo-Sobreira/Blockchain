import pyodbc #CONECTA AO SQL

class Banco_SQL:

    '''
    A fim de facilitar a comunicação com o banco de dados, está classe a interação para extrairmos as
    informações necessárias na criação da Blockchain.

    1° Método -> Passa o nome da tabela a ser consultada.
    2° Método -> Conecta o programa com o banco de dados escolhido.
    3° Método -> Após a conexão, com banco podemos então manipula-lo e desta manipulação sairá o arquivo que se transformará em um bloco.
    '''

    def __init__(self):
        pass

    def conectar_banco(self):

        #DADOS DE CONEXÃO PARTICULAR
        sgbd = "*********"
        servidor = "************"
        nome_banco = "************"
        ususario = "*******"
        senha = "******"

        #FAZ CONEXÃO COM O BANCO
        conexao = pyodbc.connect(f"DRIVER={sgbd};SERVER={servidor};DATABASE={nome_banco};UID={ususario};PWD={senha}")
        return conexao

    def manipular_banco(self,tabela):

        cursor = self.conectar_banco().cursor()

        #PODEMOS ALTERAR A VONTADE
        comando = f"""SELECT *
        FROM {tabela}"""

        cursor.execute(comando)

        #RETORNA O N° DE LINHAS SELECIONADOS
        return cursor.fetchall()
