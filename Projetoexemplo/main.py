from flask import Flask, render_template, redirect, request

app = Flask(__name__)

filmes = []

@app.route('/')
def mais():
    return render_template('mais.html', filmes=filmes)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    """
    adicionando um novo contato.
    """
    if request.method == 'POST':
        filme1 = request.form['Divertida mente']
        filme2 = request.form['À procura da felicidade']
        filme3 = request.form['Missão impossível']
        filme4 = request.form['Gente grande']
        filme5 = request.form['Amor em obras']
        filme6 = request.form['O céu é de verdade']
        codigo = len(filmes)
        filmes.append([codigo, filme1, filme2, filme3, filme4, filme5, filme6])
        return redirect('/mais.html')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_filme.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):

   # Editando um filme existente

    if request.method == 'POST':
        filme1 = request.form['Divertida mente']
        filme2 = request.form['À procura da felicidade']
        filme3 = request.form['Missão impossível']
        filme4 = request.form['Gente grande']
        filme5 = request.form['Amor em obras']
        filme6 = request.form['O céu é de verdade']
        filmes[codigo] = [codigo, filme1, filme2, filme3, filme4, filme5, filme6]
        return redirect('/mais.html')  # Redirecionando para a página inicial
    else:
        filme = filmes[codigo]
        return render_template('editar_filme.html', filme=filme)  # Renderiza o formulário de edição

@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/mais.html')  # Redireciona de volta para a página inicial

if __name__ == '__main__':
    app.run(debug=True)
