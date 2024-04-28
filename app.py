from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

@app.route('/')
def index():
    return render_template ('index.html')

usuarios = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui verificamos se os campos obrigatórios foram preenchidos:
        if 'username' in request.form and 'email' in request.form:
            # Obtém os dados do formulário:
            username = request.form['username']
            email = request.form['email']
            
            # Enviar dados para a API como formulário codificado:
            api_url = "http://127.0.0.1:5000/api/register"
            data = {'username': username, 'email': email}
            try:
                response = requests.post(api_url, data=data)  # Enviar dados como formulário codificado
                if response.status_code == 200:
                    flash('Dados cadastrados com sucesso na API.', 'success')
                else:
                    flash('Erro ao cadastrar dados na API.', 'error')
            except requests.exceptions.RequestException as e:
                flash(f'Erro de conexão com a API: {e}', 'error')
            
            return redirect(url_for('register'))
        else:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')

    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def register_api():
    if request.method == 'POST':
        # OBTER os dados do formulário codificado:
        data = request.form
        
        # Verificamos se os dados estão presentes e são válidos:
        if data and 'username' in data and 'email' in data:
            # Obter o nome de usuário e o e-mail do formulário:
            username = data['username']
            email = data['email']

            # Essa lógica de cadastro é bem simples (apenas imprime os dados)
            print(f'Dados recebidos da aplicação Flask: {username}, {email}')

            # Adiciona os dados à lista de usuários
            usuarios.append({'username': username, 'email': email})
            # Retorna uma resposta de sucesso para a aplicação Flask
            return jsonify({'message': 'Dados cadastrados com sucesso na API'}), 200
        else:
            # Se os dados estiverem ausentes ou inválidos, retorna um erro 400 (Bad Request)
            return jsonify({'error': 'Dados inválidos'}), 400

    # Se a solicitação não for POST, retorne um erro 405 (Método não permitido)
    return jsonify({'error': 'Método não permitido'}), 405

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    # Retorna a lista de usuários cadastrados
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
