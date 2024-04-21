Aquí tienes el README.md con un formato mejorado:

markdown
Copy code
# proyectog

## Estructura del Repositorio

El repositorio cuenta con la siguiente estructura, simplificada para su comprensión:

proyectog/
├── backend/
│ ├── backendapp/
│ ├── backend_project/
├── backend-chart/
│ ├── Chart.yaml
│ ├── templates/
│ │ ├── deployment.yaml
│ │ ├── _helpers.tpl
│ │ └── service.yaml
│ └── values.yml
├── create_project.py
├── docker-compose.yml
├── Dockerfile
├── gui/
│ ├── guiapp/
│ │ └── templates/
│ │ └── guiapp/
│ │ └── formulario.html
│ └── gui_project/
├── gui-chart/
│ ├── Chart.yaml
│ ├── templates/
│ │ ├── deployment.yaml
│ │ ├── _helpers.tpl
│ │ └── service.yaml
│ └── values.yml
├── nginx/
│ ├── Dockerfile
│ └── nginx.conf
├── nginx-chart/
│ ├── Chart.yaml
│ ├── templates/
│ │ ├── deployment.yaml
│ │ ├── _helpers.tpl
│ │ └── service.yaml
│ └── values.yml
├── README.md
├── requirements.txt
└── venv/

makefile
Copy code

Para cada contenedor, se proporcionan los directorios de los proyectos Django con sus respectivos Dockerfiles, así como los directorios de los chart de Helm con sus templates.

## Ejecución Local

Para ejecutar el ambiente en Docker con Docker-compose (ambiente local):

1. Descargar el repositorio.
2. Ingresar al directorio `/proyectog/proyectog` y ejecutar `docker-compose -f "docker-compose.yml" build`.
3. Una vez creado el build, ejecutar `docker-compose -f "docker-compose.yml" up`.

Si se está en Docker, modificar el archivo `formulario.html` y cambiar la IP en las funciones de JavaScript a: `http://0.0.0.0:8002`.

## Ejecución en Minikube (Kubernetes)

Primero, se deben establecer las credenciales o secrets en Github:

```bash
ARGOCD_PASSWORD="password_argocd"
ARGOCD_SERVER="ip_argo_cd"
ARGOCD_TOKEN="toke_argo_cd"
ARGOCD_USERNAME="user_argocd"
DOCKER_PASSWORD="password_dockerhub"
DOCKER_USERNAME="user_dockerhub"
El despliegue se realiza mediante Github Actions, cuya estructura de archivos se encuentra en el repositorio:

css
Copy code
.github/
└── workflows/
    ├── deployargo.yml
    └── main.yml
El archivo main.yml contiene los jobs necesarios para:

Realizar el build de las imágenes Docker para django-gui, django-backend, y nginx.
Subir las imágenes a DockerHub.
El archivo deployargo.yml, que depende de main.yml, realiza el sync en ArgoCD. Es imperativo configurar ArgoCD antes de desplegar. Utiliza la URL del repositorio Github y toma los datos como el nombre de la rama, el path, etc.

Luego de crear los pods, se deben ejecutar los archivos service en Minikube para realizar la exposición y permitir el acceso por navegador.

Ejecutar service.yaml y servicenginx.yaml que se encuentran en la raíz del repositorio:

bash
Copy code
kubectl apply -f service.yaml
kubectl apply -f servicenginx.yaml
Finalmente, puedes verificar los servicios expuestos ejecutando:

bash
Copy code
minikube service list
Enlaces de Acceso
Backend Swagger: http://192.168.49.2:31828/docs/
Frontend: http://192.168.49.2:30759
Nginx: http://192.168.49.2:30646
Por falta de tiempo, no se pudo crear un servidor DNS que permita actuar debido a la configuración en nginx.
