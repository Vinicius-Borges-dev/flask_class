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
    user = {"username": "Miguel"}
    return render_template("index.html", user=user["username"])


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


if __name__ == "__main__":
    app.run(debug=True)
