import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "ignaciogasco22@gmail.com"
EMAIL_HOST_PASSWORD = "smiprkqqhpkxicai"  # todo junto, sin espacios

def enviar_notificacion(usuario):
    try:
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

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, usuario.email, mensaje.as_string())

        print(f"🔔 [Notificaciones] Correo enviado a {usuario.email}")
        return True
    except Exception as e:
        print("❌ Error al enviar correo:", e)
        traceback.print_exc()  # 👉 Esto muestra el error completo
        return False
