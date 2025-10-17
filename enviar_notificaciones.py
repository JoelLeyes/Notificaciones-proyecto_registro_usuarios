from django.core.mail import send_mail
from django.conf import settings

def enviar_notificacion(nombre, email, telefono):
    asunto = 'Nuevo usuario registrado'
    mensaje = f'Se ha registrado un nuevo usuario:\n\nNombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}'
    destinatario = ['admin@tuservidor.com']  # o el correo del administrador

    try:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, destinatario, fail_silently=False)
        return True
    except Exception as e:
        print(f'Error al enviar correo: {e}')
        return False
