from flask import Flask


app=Flask("hello")

@app.route("/")

def hello():
    return "Hello World"


@app.route("/contatos")

def contatos():
    return "Geyson"