from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api', methods=['GET'])
def hello():
    return jsonify({'message': 'Resolução da AC 03 de Frameworks fullstack!!'})

if __name__ == '__main__':
    app.run(debug=True)