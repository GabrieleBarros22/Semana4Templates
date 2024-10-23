from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/avaliacao')
def avaliacao():
    return render_template('avaliacao.html', current_time=datetime.utcnow())

@app.route('/identificacao')
def identificacao():
    return render_template('identificacao.html')

@app.route('/contextorequisicao')
def contextorequisicao():
    return render_template('contextorequisicao.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
