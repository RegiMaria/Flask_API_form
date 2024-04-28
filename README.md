<h4> Mini projeto em flask: Formulário </h4>
**Objetivo:**
- Um aplicativo básico de cadastro de usuário com campos para nome e email.

- Tratamento de dados de formulário e envio para API.

- Manipulação dos dados com request.form

**Funcionalidades:**
- Cadastro de Usuário:
Funcionalidade que permite aos usuários preencher um formulário com seu nome de usuário e e-mail para se cadastrar no aplicativo.
Feedback Visual:
- Funcionalidade que fornece feedback visual aos usuários indicando campos obrigatórios não preenchidos antes do envio do formulário.
- 
- Mensagem de Confirmação:
Funcionalidade que exibe uma mensagem de flash para confirmar que o cadastro foi realizado com sucesso após o envio bem-sucedido do formulário.

- Redirecionamento:
Funcionalidade que redireciona os usuários de volta para a página inicial do aplicativo após o envio bem-sucedido do formulário.

**Recursos:**
- Página inicial com com botão para o formulário de cadastro.

- Formulário para cadastro.

- Validação de Entrada: Recurso que define os campos de nome de usuário e e-mail como obrigatórios, garantindo que os usuários forneçam essas informações antes de enviar o formulário.

<h4>Pacotes:</h4>
- pip install flask

Vamos usar apenas esse, embora tanto o **flask** quanto o python tenham extensão e lib(flask-WTF e WTforms)
para simplificar a criação e validação do formulário, nós vamos estar manipulando os dados do formulário diretamente 
com o objeto **request** do Flask. 

Sobre a dinâmica de formulário e o tratamento de dados do formulário, consulte o doc.



