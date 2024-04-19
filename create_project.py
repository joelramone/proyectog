"""
funcion para crear los proyectos de django
"""
import os
import subprocess
from dotenv import *


#defino las variables

#env = Env()
#env.read_env()  # read .env file, if it exists
load_dotenv('.env')

config = load_dotenv(".env")

# Obtener los valores de las variables de entorno para projecto
project_names=os.getenv("PROJECT_NAME").split()
project_paths = os.getenv("PROJECT_PATH").split()

# Obtener los valores de las variables de entorno para apps
app_names=os.getenv("APP_NAME").split()
app_paths = os.getenv("APP_PATH").split()

# Verificar que las listas tengan la misma longitud
if len(project_names) != len(project_paths):
    print("Error: las listas 'NAME' y 'PATH' deben tener la misma longitud.")
    exit(1)
"""
# Ejecutar el comando con cada par nombre-ruta
for name, path in zip(project_names, project_paths):
    print(f"Creando project {name} en el archivo {path} ")
    comando = f'django-admin startproject {name} {path}'
    subprocess.run(comando, shell=True)
"""

# Verificar que las listas tengan la misma longitud
if len(app_names) != len(app_paths):
    print("Error: las listas 'NAME' y 'PATH' deben tener la misma longitud.")  
    exit(1)

# Ejecutar el comando con cada par nombre-ruta
for aname, apath in zip(app_names, app_paths):
    print(f"Crendo la app {aname} en el directorio {apath} ")
    subprocess.run(f'cd {apath}',shell=True)
    print(f'cd {apath}')
    subprocess.run('ls',shell=True)
    subprocess.run(f'mkdir {apath}/{aname}', shell=True) 
    subprocess.run('ls',shell=True)
    subprocess.run(f'cd {aname}',shell=True)
    print(f'cd {aname}')
    comando = f'python3 mange.py startapp {aname}'
    print(f'python3 mange.py startapp {aname}')
    #print(f'python3 mange.py startapp {aname} {apath}/{aname}')
    subprocess.run(comando, shell=True)
    # subprocess.run(f'cd ..', shell=True)
    #{apath}/{aname}
    
    
    




