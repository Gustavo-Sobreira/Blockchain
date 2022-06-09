from hashlib import sha256
from datetime import datetime

class Blockchain:
    '''
    Recebe-se uma informação válida qualquer, transforma-a em uma string, que virará um hash e será alocado na
    blockchain, após sua verificação.

    1° Método -> Cria a a lista que será nossa blockchain cujo nome é dona Gertrudez.
    2° Método -> Cria o Bloco Gêneses ou Bloco 0, fundamental para o início da blockchain, ele é o único bloco arbitário que nossa blockchain possuirá.
    3° Método -> Cria o nível de difículdade, quanto mais zeros(0) mais difícil é para o bloco ser minerado.
    4° Método -> Pega o ultimo hash já escrito na blockchain.
    5° Método -> Este é o método em que o hash do bloco é criado várias e várias vezes, até que ele atenda a condição de existencia proposto no terceiro método. Faz também a parte vizual do bloco.
    6° Método -> É o lugar onde aceita-se comunicação exterior, ele verifica se já existe o Bloco 0, caso não exista ele o cria e por recursão é executado novamente, desta vez com o Bloco 0 criado, faz o prosseguimento da blockchain, criando novos blocos.
    '''

    def __init__(self):
        self.blockchain = []
        self.cores = 0

    def criar_bloco_genesis(self):
        conteudo = 'Aceitas broa com café?'
        horario = datetime.utcnow().timestamp()
        hash_anterior = 0
        tamanho = "GENESIS"
        self.cria_bloco_em_hash(
            conteudo, horario, hash_anterior, tamanho
        )

    def dificuldade_mineracao(self, hash):
        return hash.startswith('00')

    def ultimo_hash(self):
        return self.blockchain[len(self.blockchain) - 1]

    def cria_bloco_em_hash(self, conteudo, horario, hash_anterior, tamanho):
        hash = ''
        nonce = 1
        while not self.dificuldade_mineracao(hash):
            novo_bloco = '{}:{}:{}:{}:{}'.format(
                conteudo, horario, hash_anterior, tamanho, nonce
            )
            hash = sha256(novo_bloco.encode()).hexdigest()
            print(hash)#Apagar --------------
            nonce += 1

        if self.cores == 0:
            cor = "\033[1;30;104m "
            cor2 = "\033[1;30;102m "
            self.cores +=1
        else:
            cor = "\033[1;30;102m "
            cor2 = "\033[1;30;104m "
            self.cores -= 1

        print(f"""
            -----  BLOCO {tamanho}  -----
            NONCE:{nonce}
            HASH ANTERIOR: {cor}{hash_anterior}\033[m 
            HASH ATUAL:    {cor2}{hash}\033[m 
            CONTEUDO: {conteudo}
""")
        self.blockchain.append(hash)

    def novo_bloco(self, conteudo):
        if len(self.blockchain) == 0:
            self.criar_bloco_genesis()

        tamanho = len(self.blockchain)
        hash_anterior = self.ultimo_hash()
        horario = datetime.utcnow().timestamp()
        self.cria_bloco_em_hash(
            conteudo, horario, hash_anterior, tamanho
        )
