from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random 
import account as acc

def send_mail(email,assunto, texto): # Define como vai ser o texto enviado, necessario colocar assunto e texto
    server = "smtp.gmail.com"
    port = 587
    username = acc.username
    password = acc.password

    mail_from = "Code Delivery"
    mail_to = email
    mail_subject = assunto
    mail_body = texto

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = mail_to
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText(mail_body, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mensagem)
    connection.quit()
    
