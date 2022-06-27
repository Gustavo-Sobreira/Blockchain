import json
from blockchain import BlockchainChanges
from flask import Flask, request
blockchain = BlockchainChanges()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def manipulate_json():
    #RECEBE UM OBJETO VIA POST, CONVERTE PARA JSON, PASSANDO O CONTEUDO PARA OPÇÕES DE USUÁRIOS
    if request.method == 'POST':
        informations = request.get_json()
        content = json.dumps(informations)
        blockchain.new_block(content)

        return "Solicitação via método POST"
    else:
        return 'Solicitação via método GET'

if __name__ == "__main__":
        app.run(debug=True, port=8080)
