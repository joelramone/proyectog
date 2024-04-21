# proyectog
A continuación se detallan los pasos a seguir para la instalación de los ambientes.
Dentro del repositorio tenmos la siguiente estrucura (está simplificada ya que el árbol es muy extenso y la estructura de 
los directorios son similares)

├── backend
│   ├── backendapp
│   ├── backend_project
├── backend-chart
│   ├── Chart.yaml
│   ├── templates
│   │   ├── deployment.yaml
│   │   ├── _helpers.tpl
│   │   └── service.yaml
│   └── values.yml
├── create_project.py
├── docker-compose.yml
├── Dockerfile
├── gui
│   ├── guiapp
│   │   ├── templates
│   │   │   └── guiapp
│   │   │       ├── formulario.html
│   ├── gui_project
├── gui-chart
│   ├── Chart.yaml
│   ├── templates
│   │   ├── deployment.yaml
│   │   ├── _helpers.tpl
│   │   └── service.yaml
│   └── values.yml
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── nginx-chart
│   ├── Chart.yaml
│   ├── templates
│   │   ├── deployment.yaml
│   │   ├── _helpers.tpl
│   │   └── service.yaml
│   └── values.yml
├── Radme.txt
├── README.md
├── requirements.txt
├── venv
├── venv.dev
├── venv.prod

Por cada contenedor tenemos:
-Los directorios de los proyectos django con sus respectivos Dockerfile.
-Los directorios de de chart de helm con sus templates
ejemplo:
-django-backend contiene su dockerfile, los archivos necesarios para levantar el ambiente django,
la app donde se desarrolla el proyecto.
-backend-chart contiene los cahrt de helm y templates para poder ejecutar desde ArgoCD el despliegue a minikube (KB8)

También contamos con el directorio para nginx y el chart de heml para desplegar en minikube nginx

A su vez podremos encontrar el archivo docker-compose.yml que servirá para levantar los contenedores docker.


#EJECUCION LOCAL:

Para ejecutar el ambiente en Docker con Docker-compose (ambiente local)

Descargar el repositorio
Ingresar al directorio /proyectog/proyectog y ejecutar docker-compose -f "docker-compose.yml" build
Una vez creado el build ejecutar docker-compose -f "docker-compose.yml" up

Si estamos en Docker modificar el archivo formulario.html y cambiar la ip en las funciones de javascript a:
http://0.0.0.0:8002

#EJECUCION EN MINIKUBE (kubernetes)

Primero debemos setear las credenciales o secrets en github.

ARGOCD_PASSWORD="password_argocd"
ARGOCD_SERVER="ip_argo_cd"
ARGOCD_TOKEN="toke_argo_cd"
ARGOCD_USERNAME="user_argocd"
DOCKER_PASSWORD="password_dockerhub"
DOCKER_USERNAME="user_dockerhub"

El despliegue se realiza mediante github actions
cuya estructura de archivos la encontramos en el repositorio:

.github/
└── workflows
    ├── deployargo.yml
    └── main.yml

main es el workflow con los jobs necesarios para 
-realizar el build de las imagenes docker
 .django-gui
 .django-backend
 .ningx
-subir las imágenes a dockerhub

*NOTA:* por razones de tiempo, se decidió utilizar la base de datos que vine por defecto en django
a saber sqlite3. De ser necesario utilizar otra base de datos se debería agregar  a docker compose los 
datos necesarios y también al workflow. De preferncia utilizo postgresql.


Luego el workflow deployargo.yml que depende de main.yml (es decir que on entrará en ejecución hasta que main finalice)
realiza el sync en Argocd
Es importante aclarar, que es imperativo configurar ArgoCd antes de desplegar.
Para ello utilizaremos la url del repositorio Github y de ahí tomaremos los datos como nombre de rama, Path etc.


Luego de crear los pods, devemos ejecutar los archivos service en minikub, los cuales nos harán la exposición para poder ingresar por navegador

Ejecutar service.yaml  y servicenginx.yaml que se encuentran en el razi del repo.


minikube service list


#Backend Swagger
http://192.168.49.2:31828/docs/

#Frontend
http://192.168.49.2:30759

#Nginx

http://192.168.49.2:30646 

Por falta de tiempo no pude crear un servidor dns que  permita actuar debido a la configuración en nginx.

