#importações
from flask import Flask #importando framework Flask
from flask_sqlalchemy import SQLAlchemy #importando SQLAlchemy (biblioteca de ORM)

app = Flask(__name__) #instância do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db' #configurando banco de dados

db = SQLAlchemy(app) #iniciando o banco de dados / conexão

#modelando banco de dados
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True) #coluna de id (primary key)
  name = db.Column(db.String(120), nullable=False) #coluna de nome
  price = db.Column(db.Float, nullable=False) #coluna de preço
  description = db.Column(db.Text, nullable=True) #coluna de descrição (opcional)

#definindo rota raiz e função executada ao acessá-la
@app.route('/')
def hello_world():
  return "Hello World" #mensagem simples

#verificando se o script está sendo executado diretamente
if __name__ == "__main__":
  app.run(debug=True) #rodando aplicação com debug (exibe erros detalhados)