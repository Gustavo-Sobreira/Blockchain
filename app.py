import usuario
from flask import Flask, request, redirect,render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def manipula_json():
    #RECEBE O JSON E O PASSA PARA A BLOCKCHAIN
    informacoes = request.json.get("informacoes")
    usuario.iniciar_projeto(informacoes)
    return redirect('/')

if __name__ == "__main__":
        app.run(debug=True, port=8080)
