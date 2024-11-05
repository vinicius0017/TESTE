from flask import Flask, render_template



app = Flask (__name__)

@app.route('/')
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')



@app.route("/Perfil/<nome_usuario>")
def Perfil_usuario(nome_usuario):
    return  render_template("Perfil_usuario.html", nome_usuario=nome_usuario)


if __name__ =="__main__":
    app.run(debug=True)
