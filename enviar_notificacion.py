import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP de Gmail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "serverinfra1@gmail.com"  # Tu correo de Gmail
EMAIL_HOST_PASSWORD = "iwsj ckyn narr opee"       # Tu contraseña o contraseña de aplicación

def enviar_notificacion(usuario):
    try:
        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = EMAIL_HOST_USER
        mensaje["To"] = usuario.email
        mensaje["Subject"] = "¡Bienvenido!"
        cuerpo = f"""
        Hola {usuario.nombre},

        Gracias por registrarte. Nos alegra tenerte con nosotros.

        Saludos,
        El equipo de Notificaciones
        """
        mensaje.attach(MIMEText(cuerpo, "plain"))

        # Conectar al servidor SMTP
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Iniciar conexión segura
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, usuario.email, mensaje.as_string())

        print(f"🔔 [Notificaciones] Correo enviado a {usuario.email}")
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False