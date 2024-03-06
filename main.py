from flask import Flask, render_template, request, flash, redirect
import json


app = Flask(__name__)
app.config['SECRET_KEY']= "password"

@app.route("/")
def home():
    return render_template("html/login.html")

@app.route("/adm")

@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for c in lista:
            cont+=1
            if usuario == 'adm' and senha == '000':
                return redirect('/adm')
            if usuario == c['nome'] and senha == c['senha']:
                return render_template("html/acesso.html", nomeUsuario=c['nome'])
            if cont >= len(lista):
                flash('Usuario inválido')
                return redirect("/")


if __name__ in '__main__':
    app.run(debug=True)