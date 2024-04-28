import secrets

# Gerar uma chave secreta aleatória
secret_key = secrets.token_hex(16)
print("Chave secreta:", secret_key)

# Defindo como variável de ambiente
setx FLASK_SECRET_KEY= "FLASK_SECRET_KEY"
Chave secreta: 'secret_key'
set FLASK_SECRET_KEY="secret_key"