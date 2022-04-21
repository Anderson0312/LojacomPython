from flask import Flask, render_template

app = Flask(__name__)

# route -> meusite.com/
# função -> oque voce quer exivir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contas")
def contas():
    return render_template("contas.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    #sevidor do heroku