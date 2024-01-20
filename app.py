from flask import Flask, jsonify

app = Flask (__name__)


@app.route('/<int:id>', methods=['POST'])
def pessoas(id): 
    soma = 1 + id
    return jsonify({'id':id, 'nome': 'vivi', 'profissao':'desenvolvedora'})


@app.route('/soma/<int:valor1>/<int:valor2>',  methods=['POST'])
def soma(valor1,valor2):
    return jsonify({'soma': valor1 + valor2})


if __name__=='__main___':
    app.run(debug=True)