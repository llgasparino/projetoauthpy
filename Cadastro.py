from send_email import * 
from authpy import *

def menu_cadastro():
    print("Menu de criação de conta: ")
    cadastrado = False
    validado = False
    while cadastrado != True:
        print("1. Cadastro de conta\n2. Validar E-Mail\n0. Sair")
        menu_cadastro = int(input("Digite a opção desejada: "))

        match menu_cadastro:
            case 1:
                user = input("Digite seu E-mail: ")
                password = input("Digite sua senha, com pelo menos 6 caracteres: ")
                
                # Tenta criar o usuário e envia o código de verificação
                try:
                    dados_usuario = cria_usuario(user, password)
                    if dados_usuario:
                        codigo = gerar_codigo()
                        print("Código enviado para o email do cadastro!")
                        texto = f'Seu código de verificação é: {codigo} \nUse esse código para confirmar a sua conta'
                        assunto = "Código de verificação"
                        send_mail(user, assunto, texto)
                        print("Voltando ao menu principal. Digite 2 para validar e-mail.")
                    else:
                        print("Falha no cadastro: o usuário não foi criado.")
                        continue
                except Exception as e:
                    print(f"Ocorreu um erro no processo de cadastro: {e}")
                continue
            case 2:

                codigo_digitado = int(input("Digite o código enviado no E-mail: "))
                if codigo_digitado == codigo:
                    print("Email validado com sucesso! Você está autenticado")
                    validado ==  True 
                    return cadastrado == True
                else:
                    print("Código inválido")
                    continue
                    
            case 0:
                break
            
# def menu_logado():
#     print("1. Cadastro de conta\n2. Validar email\n3. Fazer Login\n9. Sair da conta")

#     while True:
#         menu_logado = int(input("Digite a opção desejada: "))
#         match menu_logado:
#             case 1:
#                 email = input("digite seu email")
#                 print("cadastrado")
#                 codigo = gerar_codigo
#                 print("Código enviado para o email do cadastro")
#                 texto = f'Seu código de verificação é: {codigo}\nUse esse código para confirmar a sua conta'
#                 assunto = "Código de verificação"
#                 #send_mail(email,assunto,texto)
                
#                 print("-Isso não sera visivel- ", texto)
#                 print("Voltando ao menu principal, digite 1 para validar e-mail.")
#                 continue
#             case 2:

#                 codigo_digitado = int(input("Digite o código enviado no E-mail"))
#                 if codigo_digitado == codigo_digitado:
#                     print("Email validado com sucesso! Faça login para continuar.")
#                     cadastrado ==  True
                    
#                 print(random_var)
#             case 3:
#                 print('3')
#             case 9:
#                 break
