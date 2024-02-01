# API REST que possibilita: Criar, Atualizar, Listar, Deletar e Avaliar filmes;
# Dada uma lista de filmes, o sistema é capaz de indicar um filme que ainda não foi avaliado;
# Utiliza um banco de dados para armazenar as informações dos filmes;

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmes.db'
db = SQLAlchemy(app)

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    avaliacao = db.Column(db.Float)

@app.route('/filmes', methods=['GET', 'POST'])
def filmes():
    if request.method == 'GET':
        filmes = Filme.query.all()
        lista_filmes = [{'id': filme.id, 'titulo': filme.titulo, 'avaliacao': filme.avaliacao} for filme in filmes]
        return jsonify(lista_filmes)

    elif request.method == 'POST':
        dados = request.json
        novo_filme = Filme(titulo=dados['titulo'], avaliacao=dados.get('avaliacao'))
        db.session.add(novo_filme)
        db.session.commit()
        return jsonify({'mensagem': 'Filme adicionado com sucesso!'})

@app.route('/filmes/<int:filme_id>', methods=['GET', 'PUT', 'DELETE'])
def filme(filme_id):
    filme = Filme.query.get_or_404(filme_id)

    if request.method == 'GET':
        return jsonify({'id': filme.id, 'titulo': filme.titulo, 'avaliacao': filme.avaliacao})

    elif request.method == 'PUT':
        dados = request.json
        filme.titulo = dados['titulo']
        filme.avaliacao = dados.get('avaliacao')
        db.session.commit()
        return jsonify({'mensagem': 'Filme atualizado com sucesso!'})

    elif request.method == 'DELETE':
        db.session.delete(filme)
        db.session.commit()
        return jsonify({'mensagem': 'Filme deletado com sucesso!'})

@app.route('/filmes/recomendacao', methods=['GET'])
def recomendar_filme():
    filme = Filme.query.filter_by(avaliacao=None).first()
    if filme:
        return jsonify({'id': filme.id, 'titulo': filme.titulo})
    else:
        return jsonify({'mensagem': 'Nenhum filme não avaliado disponível'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
