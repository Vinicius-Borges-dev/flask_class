from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
# def index():
#     user = {'username': 'Miguel'}
#     return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html", nome="John")


@app.route("/perfil")
def perfil():
    users = {
        "nome": "John",
        "idade": 20,
        "email": "John@email.com",
    }
    return render_template("perfil.html", users=users)


@app.route("/lista/pratica")
def lista_pratica():
    lista = ["A", "B", "C"]
    return render_template("lista.html", lista=lista)


@app.route("/login/<string:usuario>/<string:senha>")
def login(usuario, senha):
    is_logged_in = False
    if usuario == "admin" and senha == "admin":
        is_logged_in = True
        return render_template("login.html", logged=is_logged_in)
    return render_template("login.html", logged=is_logged_in)


@app.route("/atividade10")
def atividade10():
    user = {"nome": "John", "idade": 32, "cidade": "Curitiba"}
    return render_template("atividade10.html", user=user)


@app.route("/atividade11")
def atividade11():
    lista = [
        {
            "nome": "John",
            "endereco": "Rua Tal",
            "telefone": "13246546",
            "email": "John@email.com",
            "cpf": "123-456-789-00",
            "tipo_de_conta": "cliente",
        },
        {
            "nome": "Maria",
            "endereco": "Avenida XYZ",
            "telefone": "98765432",
            "email": "maria@email.com",
            "cpf": "987-654-321-00",
            "tipo_de_conta": "cliente",
        },
        {
            "nome": "Carlos",
            "endereco": "Rua Principal",
            "telefone": "55512345",
            "email": "carlos@email.com",
            "cpf": "555-123-456-00",
            "tipo_de_conta": "cliente",
        },
        {
            "nome": "Ana",
            "endereco": "Rua das Flores",
            "telefone": "99988877",
            "email": "ana@email.com",
            "cpf": "111-222-333-44",
            "tipo_de_conta": "cliente",
        },
        {
            "nome": "Pedro",
            "endereco": "Avenida Central",
            "telefone": "77744433",
            "email": "pedro@email.com",
            "cpf": "777-444-555-66",
            "tipo_de_conta": "cliente",
        },
    ]
    return render_template("atividade11.html", users=lista)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/container")
def container():
    return render_template("container.html")



if __name__ == "__main__":
    app.run(debug=True)
