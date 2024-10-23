from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

# Inicializando Bootstrap e Moment.js no Flask
bootstrap = Bootstrap(app)
moment = Moment(app)

# Tratamento de erro 404 - Página não encontrada
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Tratamento de erro 500 - Erro interno do servidor
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Rota principal - Página inicial
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

# Rota para a página de avaliação
@app.route('/avaliacao')
def avaliacao():
    return render_template('avaliacao.html', current_time=datetime.utcnow())

# Rota para a página de identificação
@app.route('/identificacao')
def identificacao():
    return render_template('identificacao.html')

# Rota para a página de contexto de requisição
@app.route('/contextorequisicao')
def contextorequisicao():
    return render_template('contextorequisicao.html')

# Rota para a página de usuário dinâmico
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Executando a aplicação no modo debug
if __name__ == '__main__':
    app.run(debug=True)
