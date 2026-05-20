import smtplib
from email.message import EmailMessage
import getpass

mensaje = EmailMessage()
mensaje["From"] = "tu_correo@example.com"
mensaje["To"] = "destinatario@example.com"
mensaje["Subject"] = "Prueba de correo desde Python"
mensaje.set_content("Hola, este es un correo enviado desde Python usando SMTP_SSL.")

smtp_server = "smtp.gmail.com"
smtp_port = 465

password = getpass.getpass("Introduce tu contraseña de aplicación: ")

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(mensaje["From"], password)
    server.send_message(mensaje)

print("Correo enviado correctamente.")



