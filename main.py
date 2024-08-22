from flask import Flask, render_template, redirect, request

app = Flask(__name__)

filmes = []

@app.route('/')
def index():
    return render_template('mais.html', filmes=filmes)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    """
    adicionando um novo filme.
    """
    if request.method == 'POST':
        nomedofilme = request.form['nome']
        codigo = len(filmes)
        filmes.append([codigo, nomedofilme])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_filme.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):

   # Editando um filme existente

    if request.method == 'POST':
        nomedofilme = request.form['nome']
        filmes[codigo] = [codigo, nomedofilme]
        return redirect('/')  # Redirecionando para a página inicial
    else:
        filme = filmes[codigo]
        return render_template('editar_filme.html', filme=filme)  # Renderiza o formulário de edição

@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

if __name__ == '__main__':
    app.run(debug=True)
