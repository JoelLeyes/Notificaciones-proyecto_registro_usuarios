# Notification Service  Flask

Microservicio que recibe peticiones `POST /notify` desde el backend y envía una notificación (correo o log). Diseñado para ejecutarse en contenedor y desplegarse en EKS como servicio interno (ClusterIP).

- Lenguaje/Framework: Python + Flask
- Puerto por defecto: 5001
- Exposición: interna (Kubernetes Service ClusterIP)

## Endpoint
- POST /notify
  - Body esperado (ejemplo):
    {
      "event": "user_created",
      "email": "usuario@example.com",
      "nombre": "Usuario",
      "telefono": "099123456"
    }

## Requisitos locales
- Python 3.11+
- pip  25

## Ejecución local
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Credenciales simuladas
$env:SMTP_HOST = "smtp.example.com"
$env:SMTP_PORT = "587"
$env:SMTP_USER = "notifier@example.com"
$env:SMTP_PASS = "simulated-strong-pass"
$env:SENDER    = "no-reply@example.com"
$env:RECIPIENT = "admin@example.com"

python app.py  # o: python -m flask --app app run -h 0.0.0.0 -p 5001
```

Probar:
```powershell
curl -X POST http://127.0.0.1:5001/notify `
  -H "Content-Type: application/json" `
  -d '{"event":"user_created","email":"usuario@example.com","nombre":"Usuario","telefono":"099"}'
```

## Contenedor Docker
```powershell
docker build -t notification-svc:local .

docker run --rm -p 5001:5001 `
  -e SMTP_HOST=smtp.example.com -e SMTP_PORT=587 `
  -e SMTP_USER=notifier@example.com -e SMTP_PASS=simulated-strong-pass `
  -e SENDER=no-reply@example.com -e RECIPIENT=admin@example.com `
  notification-svc:local
```

## Publicación en ECR (placeholders)
```powershell
$AWS_ACCOUNT_ID = "111122223333"
$AWS_REGION     = "us-east-1"
$REPO           = "proyecto/notificaciones"
$IMAGE          = "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO:latest"

aws ecr get-login-password --region $AWS_REGION | docker login `
  --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"

docker build -t $IMAGE .
docker push $IMAGE
```

## Despliegue en Kubernetes (EKS)
Service interno (ClusterIP). El backend llama vía DNS interno de k8s.

Manifiesto ejemplo (repo raíz): `k8s/notifications-deployment.yml`
```powershell
kubectl apply -f k8s/notifications-deployment.yml
kubectl get svc,pods -o wide
```

Variables de entorno típicas (simuladas):
- SMTP_HOST=smtp.example.com
- SMTP_PORT=587
- SMTP_USER=notifier@example.com
- SMTP_PASS=simulated-strong-pass
- SENDER=no-reply@example.com
- RECIPIENT=admin@example.com

## Seguridad (SSDLC)  evidencias
- SAST (Bandit), SCA (pip-audit) y SCA de imagen (Grype).
- DAST (ZAP) aplica a endpoints públicos (no a este servicio interno).
Evidencias en `evidencias/security/` del repo raíz.

---
Este README incluye credenciales simuladas a modo de ejemplo. No subir secretos reales.
