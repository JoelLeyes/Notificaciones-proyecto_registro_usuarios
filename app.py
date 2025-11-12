from flask import Flask, request, jsonify
from enviar_notificacion import enviar_notificacion


class UserObj:
    def __init__(self, nombre, email, telefono=None):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono


app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200


@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json() or {}
    nombre = data.get('nombre') or data.get('name')
    email = data.get('email')
    telefono = data.get('telefono')
    if not nombre or not email:
        return jsonify({'error': 'nombre and email required'}), 400
    user = UserObj(nombre, email, telefono)
    ok = enviar_notificacion(user)
    return jsonify({'notificado': bool(ok)}), (201 if ok else 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

