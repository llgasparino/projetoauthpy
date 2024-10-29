from send_email import * 
from authpy import *

def menu_cadastro():
    print("Menu de criação de conta: ")
    while True:
        print("1. Cadastro de conta\n2. Validar E-Mail\n3. Fazer login\n0. Sair")
        menu_cadastro = int(input("Digite a opção desejada: "))

        match menu_cadastro:
            case 1:
                user = input("Digite seu E-mail: ")
                password = input("Digite sua senha, com pelo menos 6 caracteres: ")
                iniciar_cadastro(user, password)
                continue
            case 2:
                user = input("Digite seu E-mail para verificação: ")
                codigo_inserido = input("Digite o código de verificação: ")
                finalizar_cadastro(user, codigo_inserido)
                continue
                    
            case 3:
                user = input("Digite seu E-mail: ")
                password = input("Digite sua senha: ")
                entra_usuario(user, password)
                menu_logado()
            case 0:
                break


def menu_logado():
    while True:
        print("Você está logado!")
        print("1. Sair")
        menu_logado = int(input("Selecione a opção que deseja: "))

        match menu_logado:
            case 1:
                break 
            case _:
                print("Digite 1 para sair.")
        
