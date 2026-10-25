from flask import (
    Blueprint,
    abort,
    redirect,
    render_template,
    request,
    url_for
)

from models.livro_model import (
    alterar_status,
    listar_livros
)

livros_bp = Blueprint('livros', __name__)


@livros_bp.get('/')
def inicio():
    busca = request.args.get('busca', '').strip()

    return render_template(
        'index.html',
        livros=listar_livros(busca),
        busca=busca
    )


@livros_bp.get('/desejos')
def desejos():
    return render_template(
        'desejos.html',
        livros=listar_livros(filtro='desejados')
    )


@livros_bp.get('/reservas')
def reservas():
    return render_template(
        'reservas.html',
        livros=listar_livros(filtro='reservados')
    )


@livros_bp.post('/livros/<int:livro_id>/<acao>')
def atualizar(livro_id, acao):

    campos = {
        'desejo': 'desejado',
        'reserva': 'reservado'
    }

    if acao not in campos:
        abort(404)

    if not alterar_status(livro_id, campos[acao]):
        abort(404)

    destino = request.form.get(
        'origem',
        'livros.inicio'
    )

    if destino not in (
        'livros.inicio',
        'livros.desejos',
        'livros.reservas'
    ):
        destino = 'livros.inicio'

    return redirect(url_for(destino))