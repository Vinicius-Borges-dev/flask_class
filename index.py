from flask import Flask

app = Flask(__name__)

@app.route("/test/<nome>")
def test(nome):
    return f"Olá, {nome}"

@app.route("/hello")
def hello():
    return 'Olá, mundo'

@app.route("/bye")
def bye():
    return 'Adeus, mundo'

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return f'A soma de {a} e {b} é {a + b}'

@app.route('/invert/<text>')
def invert(text):
    return text[::-1]

@app.route('/parImpar/<int:a>')
def parImpar(a):
    return f'{a} é par?: {a % 2 == 0}'

@app.route('/<operation>/<int:a>/<int:b>')
def operation(operation, a, b):
    if operation == 'soma':
        return f'Soma {a + b}'
    elif operation == 'subtração':
        return f'Subtração {a - b}'
    elif operation == 'multiplicação':
        return f'Multiplicação {a * b}'
    elif operation == 'divisão':
        return f'Divisão {a / b}'


if __name__ == '__main__':
    app.run(debug=True)