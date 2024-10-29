
from account import firebaseConfig
import pyrebase
from requests.exceptions import HTTPError
from send_email import send_mail
import random 
from typing import Dict

# Armazena as informações temporárias dos usuários
usuarios_pendentes: Dict[str, Dict[str, str]] = {}

def gerar_codigo():
    return str(random.randint(100000, 999999))

def iniciar_cadastro(user, password):
    # Gera e envia o código de verificação
    codigo = gerar_codigo()
    send_mail(user, "Código de verificação", f"Seu código de verificação é: {codigo}")
    
    # Armazena temporariamente os dados do usuário até a verificação
    usuarios_pendentes[user] = {
        "password": password,
        "codigo": codigo
    }
    print("Código de verificação enviado para o e-mail.")

def finalizar_cadastro(user, codigo_inserido):
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    
    print(f"Usuário: {user}, Código inserido: {codigo_inserido}")
    
    if user in usuarios_pendentes:
        print(f"Código enviado: {usuarios_pendentes[user]['codigo']}")
        if usuarios_pendentes[user]["codigo"] == codigo_inserido:
            try:
                password = usuarios_pendentes[user]["password"]
                auth.create_user_with_email_and_password(user, password)
                print("Usuário criado com sucesso após verificação!")
                
                del usuarios_pendentes[user]
            except HTTPError as e:
                print("Erro ao criar o usuário:", e)
                if e.response:
                    print("Resposta do servidor:", e.response.text)  # Resposta detalhada do erro
        else:
            print("Código de verificação incorreto.")
    else:
        print("Usuário não está em processo de cadastro.")
        
def entra_usuario(user, password):
    try:
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth = firebase.auth()
        auth.sign_in_with_email_and_password(user, password)
        print("Login realizado com sucesso!")
    except HTTPError as e:
        print("Erro número " + e )


