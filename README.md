# 📚 Livraria Encanto — MVC

MVP web de uma livraria desenvolvido com Python, Flask, HTML, CSS e SQLite, organizado no padrão **Model–View–Controller (MVC)**.

## Funcionalidades

- Catálogo com livros de exemplo.
- Pesquisa por título ou autor.
- Adicionar e remover livros da lista de desejos.
- Reservar e cancelar reservas.
- Persistência local com SQLite.

## Arquitetura

O projeto utiliza a arquitetura MVC, separando as responsabilidades da aplicação:

- **Model:** `models/livro_model.py` — acesso ao SQLite e regras de negócio.
- **View:** `templates/` e `static/` — páginas HTML e estilos CSS.
- **Controller:** `controllers/livro_controller.py` — rotas, requisições e respostas.
- **Inicialização:** `app.py` — registra as rotas e inicializa o banco de dados.

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- SQLite
- Git e GitHub

## Como executar

No Windows, abra o terminal na pasta do projeto e execute:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Depois, abra o endereço exibido pelo Flask no navegador.

Por padrão:

`http://127.0.0.1:5000`

## Banco de dados

O banco de dados `livraria.db` é criado automaticamente na primeira execução.

Esta versão é uma demonstração local, sem autenticação de usuários. A lista de desejos e as reservas são compartilhadas por todos que acessarem a mesma instância da aplicação.

## Objetivo acadêmico

O projeto foi desenvolvido para demonstrar a aplicação da arquitetura MVC em um sistema web de livraria, separando interface, controle de requisições e gerenciamento de dados.