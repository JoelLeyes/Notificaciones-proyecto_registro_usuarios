from enviar_notificacion import enviar_notificacion

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

if __name__ == "__main__":
    user = Usuario("Ignacio", "ignaciogasco6@gmail.com")
    enviar_notificacion(user)
