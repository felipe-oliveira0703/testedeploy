from flask import Flask, jsonify, request

app = Flask(__name__)

#exemplo que ele usa 

devs = [
    {
        'id': 1,
        'name': 'Felipe',
        'lang': 'python'
    },
    {
        'id': 2,
        'name': 'Robert Hrosher',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'John Delare',
        'lang': 'python'
    },
    {
        'id': 4,
        'name': 'John Doe',
        'lang': 'node'
    }
]
# metodo get é para quando queremos colocar algo para o usuario e pegar algo da URL 
@app.route('/devs', methods=['GET'])
def home():
    return jsonify(devs), 200


@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200


@app.route('/devs/<int:id>', methods=['PUT'])
def change_lang(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')

            return jsonify(dev), 200

    return jsonify({'error': 'dev not found'}), 404


@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200

    return jsonify({'error': 'not found'}), 404

## no metodo post a gente espera receber algo do usuario
@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json() ## aqui o data virou um 
    devs.append(data)
    # nesse momento devs e um dicionario. para iterar sobre dicionarios vou colocar um comentário
    # caso queira operar sobre as chavves do dicionario : 
    #for key in dic : ...
    #caso queira opera sobre os valores do dicionario:
    #for key in dic.values():
    #...... 
    #nessa página tem mais coisa http://excript.com/python/funcoes-dicionarios.html
    return jsonify(data), 201


@app.route('/devs/<int:id>', methods=['DELETE'])
def remove_dev(id):
    index = id - 1
    del devs[index]

    return jsonify({'message': 'Dev is no longer alive'}), 200

@app.route('/felipe/<int:id>',methods = ['GET'])
def function(id):
    return "%d" %id



if __name__ == '__main__':
    app.run(debug=True)
