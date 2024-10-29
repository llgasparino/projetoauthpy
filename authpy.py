import pyrebase
from requests.exceptions import HTTPError
from account import firebaseConfig


def cria_usuario(user, password):
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        status = auth.create_user_with_email_and_password(user, password)
        
        # Extrai informações do status
        local_id = status.get('localId')
        email = status.get('email')
        
        # Armazena informações importantes em um dicionário
        dados_usuario = {
            'localId': local_id,
            'email': email,
        }
        
        print("Usuário criado com sucesso!")
        return dados_usuario
    except HTTPError as e:
        if e.response is not None and e.response.content:
            try:
                error_json = e.response.json()
                error_message = error_json['error']['message']
                
                if error_message == "EMAIL_EXISTS":
                    print("Erro: O e-mail já está registrado. Tente fazer login ou use outro e-mail.")
                else:
                    print(f"Erro ao tentar criar o usuário: {error_message}")
            except ValueError:
                print("Erro: Não foi possível decodificar a resposta de erro.")
        else:
            print("Erro desconhecido ao tentar criar o usuário.")
            
def entra_usuario():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha: ")
    try:
        status = auth.sign_in_with_email_and_password(user, password)
        print("Login realizado com sucesso!")
        return status
    except HTTPError as e:
        error_json = e.response.json()
        error_message = error_json['error']['message']
        
        if error_message == "EMAIL_NOT_FOUND":
            print("Erro: E-mail não encontrado. Verifique o e-mail ou registre-se.")
        elif error_message == "INVALID_PASSWORD":
            print("Erro: Senha incorreta. Tente novamente.")
        else:
            print(f"Erro ao tentar entrar: {error_message}")
