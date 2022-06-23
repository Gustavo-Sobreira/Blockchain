from hashlib import sha256
from datetime import datetime
from banco import ManipularBancos

bancos = ManipularBancos()

class AlteracoesBlockchain:

    def __init__(self):
        self.cores = 0

    def dificuldade_mineracao(self, tentativa_hash):
        return tentativa_hash.startswith('0')


    def criar_bloco_genesis(self,horario,ultimo_hash):
        conteudo = 'Aceitas broa com café?'
        self.cria_novo_bloco(conteudo,horario,ultimo_hash)


    def cria_novo_bloco(self,conteudo,horario,ultimo_hash):
        hash_atual = ''
        nonce = int(horario)

        while not self.dificuldade_mineracao(hash_atual):
            novo_bloco = '{}:{}:{}:{}'.format(
                conteudo, horario, ultimo_hash, nonce)
            hash_atual = sha256(novo_bloco.encode()).hexdigest()
            nonce += 1

        if self.cores == 0:
            cor = "\033[1;30;104m "
            cor2 = "\033[1;30;102m "
            self.cores += 1
        else:
            cor = "\033[1;30;102m "
            cor2 = "\033[1;30;104m "
            self.cores -= 1

        print(f"""
                                    -----  BLOCO CRIADO -----
            NONCE:{nonce}
            HASH ANTERIOR: {cor}{ultimo_hash}\033[m 
            HASH ATUAL:    {cor2}{hash_atual}\033[m 
            CONTEUDO: {conteudo}
""")
        bancos.gravar_dado_blockchain(ultimo_hash,hash_atual,nonce,conteudo)


    def novo_bloco(self,conteudo):

        horario = datetime.utcnow().timestamp()
        ultimo_hash = bancos.pegar_ultimo_hash()
        if ultimo_hash == 0:
            self.criar_bloco_genesis(horario,ultimo_hash)

            #PARA CONTINUAR COM OS DADOS CHAMAMOS O HASH NOVAMENTE E CRIMOS UM NOVO BLOCO
            ultimo_hash = bancos.pegar_ultimo_hash()
            self.cria_novo_bloco(conteudo, horario, ultimo_hash)
        else:
            self.cria_novo_bloco(conteudo, horario, ultimo_hash)