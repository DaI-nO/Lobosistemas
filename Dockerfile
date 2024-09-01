# Utiliza una imagen oficial de Python
FROM python:3.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos y asegura que las dependencias estén instaladas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente del proyecto al directorio de trabajo
COPY . .

# Expone el puerto en el que se ejecutará la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
