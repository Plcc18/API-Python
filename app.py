#importações
from flask import Flask, request, jsonify #importando framework Flask, função request e jsonify
from flask_sqlalchemy import SQLAlchemy #importando SQLAlchemy (biblioteca de ORM)

app = Flask(__name__) #instância do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db' #configurando banco de dados

db = SQLAlchemy(app) #iniciando o banco de dados / conexão

#modelando banco de dados
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True) #coluna de id (primary key)
  name = db.Column(db.String(120), nullable=False) #coluna de nome
  price = db.Column(db.Float, nullable=False) #coluna de preço
  description = db.Column(db.Text, nullable=True) #coluna de descrição (opcional)

#definindo rota para adicionar livros
@app.route('/api/books/add', methods=["POST"]) #local da rota e método
def add_book(): #função para dicionar livros
  data = request.json #dados requisitados em json
  if 'name' in data and 'price' in data: #condicional que verifica se as chaves existem
    book = Book(name=data["name"], price=data["price"], description=data.get("description", "")) #obtendo informações do livro
    db.session.add(book) #adicionando livro ao banco de dados
    db.session.commit() #comitando
    return jsonify({"message": "Book added successfully"}) #retorno de cadastro
  return jsonify({"message": "Invalid book data"}), 400 #retorno de erro

#definindo rota para deletar livros
@app.route('/api/books/delete/<int:book_id>', methods=["DELETE"])
def delete_book(book_id): #função para deletar livros
  book = Book.query.get(book_id) #variável que busca o id do livro
  if book: #condicional que verifica se o id existe
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}) #retorno de deleção
  return jsonify({"message": "Book not found"}), 404 #retorno de erro

#definindo rota para exibir detalhes de um livro pelo id
@app.route('/api/books/<int:book_id>', methods=["GET"]) 
def get_book_details(book_id): #função para buscar livros
  book = Book.query.get(book_id) #variável que busca o id do livro
  if book: #condicional que verifica se o id existe
    #retorno de dados em json
    return jsonify({
      "id": book.id,
      "name": book.name,
      "price": book.price,
      "description": book.description
    })
  return jsonify({"message": "Book not found"}), 404 #retorno de erro

#definindo rota para atualizar um livro pelo id
@app.route('/api/books/update/<int:book_id>', methods=["PUT"])
def update_book(book_id): 
  book = Book.query.get(book_id)
  if not book: #condicional que verifica se não existe livro
    return jsonify({"message": "book not found"}), 404 #retorno de erro 
  
  data = request.json #dados requisitados em json
  # condicionais que verificam os dados para serem atualizados
  if 'name' in data:
    book.name = data['name']

  if 'price' in data:
    book.price = data['price']
    
  if 'description' in data:
    book.description = data['description']

  db.session.commit() #comitando
  return jsonify({"message": "Book update successfully"}) #retorno de atualização

#definindo rota raiz e função executada ao acessá-la
@app.route('/')
def hello_world():
  return "Hello World" #mensagem simples

#verificando se o script está sendo executado diretamente
if __name__ == "__main__":
  app.run(debug=True) #rodando aplicação com debug (exibe erros detalhados)