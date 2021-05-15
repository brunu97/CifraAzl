import json
from flask import Flask, render_template, Response, send_file, request, url_for
from werkzeug.utils import redirect

import Azl

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/decifrar", methods=['GET'])
def pgdecifrar():
    return render_template("decifrar.html")


@app.route("/cifrar", methods=['GET'])
def pgcifrar():
    return render_template("cifrar.html")


@app.route("/decifra", methods=['POST'])
def decifraMsg():
    if request.method == 'POST':
        r = request.json
        mensagem_cifrada = r['cifra']
        senha = r['senha']
        if any(mensagem_cifrada.isalpha() for c in mensagem_cifrada):
            return json.dumps({'mensagem': "Isto não é uma cifra Az/ reconhecível."})

        if len(senha) and len(mensagem_cifrada) > 0:
            msg = Azl.Decifra(mensagem_cifrada, senha)
            return json.dumps({'mensagem': msg})
        else:
            return json.dumps({'mensagem': "É necessário uma senha e uma mensagem cifrada."})


@app.route("/cifra", methods=['POST'])
def cifraMsg():
    if request.method == 'POST':
        r = request.json
        mensagem = r['mensagem']
        senha = r['senha']
        if len(senha) and len(mensagem) > 0:
            cifra = Azl.Cifra(mensagem, senha)
            return json.dumps({'cifra': cifra})
        else:
            return json.dumps({'cifra': "É necessário uma senha e uma mensagem."})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
