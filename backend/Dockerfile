# Establece la imagen base
FROM python:3.9

RUN mkdir /code
# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia los archivos de requerimientos (requirements.txt) al contenedor
ADD requirements.txt /code/

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el código fuente del proyecto al contenedor
ADD . /code/

# Expone el puerto en el que se ejecuta el proyecto Django
EXPOSE 8000

# Define el comando para ejecutar el proyecto Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
