from flask import Flask, render_template


app=Flask("hello")

@app.route("/")

def usuario():
    usuario=[1,"Geyson", "Dr"]
    return render_template("index.html", usuario=usuario)


@app.route("/contatos")

def contatos():
    nomeAula="Aula python para web"

    return render_template("index.html",usuario=usuario,nome=nomeAula)