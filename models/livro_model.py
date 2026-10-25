import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / 'livraria.db'

LIVROS_INICIAIS = [
    ('Orgulho e Preconceito', 'Jane Austen', 'Romance'),
    ('O Hobbit', 'J. R. R. Tolkien', 'Fantasia'),
    ('Dom Casmurro', 'Machado de Assis', 'Clássico'),
    ('Anne de Green Gables', 'L. M. Montgomery', 'Ficção'),
    ('A Revolução dos Bichos', 'George Orwell', 'Ficção'),
    ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Fábula'),
]


def conectar():
    conexao = sqlite3.connect(DB)
    conexao.row_factory = sqlite3.Row
    return conexao


def iniciar_banco():
    with conectar() as conexao:
        conexao.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                genero TEXT NOT NULL,
                desejado INTEGER NOT NULL DEFAULT 0,
                reservado INTEGER NOT NULL DEFAULT 0
            )
        ''')

        quantidade = conexao.execute(
            'SELECT COUNT(*) FROM livros'
        ).fetchone()[0]

        if quantidade == 0:
            conexao.executemany(
                'INSERT INTO livros (titulo, autor, genero) VALUES (?, ?, ?)',
                LIVROS_INICIAIS
            )


def listar_livros(busca='', filtro=None):
    consulta = '''
        SELECT * FROM livros
        WHERE (titulo LIKE ? OR autor LIKE ?)
    '''

    parametros = [f'%{busca}%', f'%{busca}%']

    if filtro == 'desejados':
        consulta += ' AND desejado = 1'

    elif filtro == 'reservados':
        consulta += ' AND reservado = 1'

    consulta += ' ORDER BY titulo'

    with conectar() as conexao:
        return [
            dict(livro)
            for livro in conexao.execute(
                consulta, parametros
            ).fetchall()
        ]


def alterar_status(livro_id, campo):
    if campo not in ('desejado', 'reservado'):
        raise ValueError('Campo inválido')

    with conectar() as conexao:
        cursor = conexao.execute(
            f'''
            UPDATE livros
            SET {campo} =
                CASE WHEN {campo} = 1 THEN 0 ELSE 1 END
            WHERE id = ?
            ''',
            (livro_id,)
        )

        return cursor.rowcount > 0