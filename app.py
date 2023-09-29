from flask import Flask,render_template

app = Flask(__name__)

# criar a 1ª pagina do site
# route -> meuportifolio.com.br
# função -> o que eu quero exibir na pagina

@app.route("/")
def homepage():
    return render_template ("index.html")

# colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)