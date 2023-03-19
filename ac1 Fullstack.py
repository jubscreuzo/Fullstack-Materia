from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/calcular_media', methods=['GET'])
def calcular_media():
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    media = (nota1 + nota2) / 2
    return render_template('resultado.html', nota1=nota1, nota2=nota2, media=media)

if __name__ == '__main__':
    app.run(debug=True)
