from flask import Flask #importando framework Flask

app = Flask(__name__) #instância do Flask

#definindo rota raiz e função executada ao acessá-la
@app.route('/')
def hello_world():
  return "Hello World" #mensagem simples

#verificando se o script está sendo executado diretamente
if __name__ == "__main__":
  app.run(debug=True) #rodando aplicação com debug (exibe erros detalhados)