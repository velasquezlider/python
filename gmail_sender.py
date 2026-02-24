import smtplib
import os
from email.message import EmailMessage

def send_email(subject, body, to_email):
    """
    Envía un correo electrónico usando Gmail SMTP y una App Password.
    """
    # Obtener credenciales de variables de entorno (recomendado)
    # También puedes hardcodearlas temporalmente para probar, pero NO es seguro.
    gmail_user = os.environ.get('GMAIL_USER')
    gmail_password = os.environ.get('GMAIL_APP_PASSWORD')

    if not gmail_user or not gmail_password:
        print("Error: Las variables de entorno GMAIL_USER y GMAIL_APP_PASSWORD no están configuradas.")
        print("Usa: export GMAIL_USER='tu_correo@gmail.com'")
        print("Usa: export GMAIL_APP_PASSWORD='tu_app_password_de_16_caracteres'")
        return

    # Crear el mensaje
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to_email

    try:
        # Conectar al servidor SMTP de Gmail (SSL)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gmail_user, gmail_password)
            smtp.send_message(msg)
            print(f"Correo enviado exitosamente a {to_email}!")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    # Ejemplo de uso
    destinatario = "tu_correo_destino@ejemplo.com" # Cambia esto
    asunto = "Prueba desde Python"
    mensaje = "Hola, este es un correo enviado automáticamente desde un script de Python."
    
    send_email(asunto, mensaje, destinatario)
