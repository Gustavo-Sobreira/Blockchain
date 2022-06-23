import usuario
from flask import Flask, request, redirect,render_template


app = Flask(__name__)

@app.route('/', methods=['POST'])
def receber_dados_crud():
    id = request.json.get("cod_funcionario")
    nome = request.json.get("usuario")
    setor = request.json.get("setor")
    acao = request.json.get("acao")
    data_hora = request.json.get("data_hora")

    arquivo_total = [id,nome,setor,data_hora,acao]
    listar_arquivo = ["Id ","Nome ",'Setor ', "Horário ", "Ação "]

    for i in range(len(arquivo_total)):
        print(f"{listar_arquivo[i] :10} =  {arquivo_total[i]}")

    usuario.iniciar_projeto(arquivo_total)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
