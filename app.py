from flask import Flask
from controllers.livro_controller import livros_bp
from models.livro_model import iniciar_banco

app = Flask(__name__)

app.register_blueprint(livros_bp)

iniciar_banco()

if __name__ == '__main__':
    app.run(debug=True)