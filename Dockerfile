# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del microservicio al contenedor
COPY . /app

# Actualiza pip a versión segura y luego instala dependencias
RUN pip install --no-cache-dir --upgrade pip==25.3 && \
    pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre Flask
EXPOSE 5001

# Comando para iniciar la aplicación Flask
CMD ["python", "app.py"]