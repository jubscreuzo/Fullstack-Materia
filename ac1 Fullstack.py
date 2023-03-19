from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calcular_media/<float:nota1>/<float:nota2>')
def calcular_media(nota1,nota2):
    media = (nota1 + nota2) / 2
    return jsonify ({'media':media})

if __name__ == '__main__':
    app.run(debug=True)
