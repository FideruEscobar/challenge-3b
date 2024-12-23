# challenge-3b
## Author: Luis Fidel Escobar Ambrosio

## Resume

Esta es una API rest creada con Django Rest framework
y como Gestor de Base de datos usa sqllite, por lo tanto
no se necesita conectarse a una base de datos y tampoco
se necesita de algun tipo de aunthenticacion.

Esta APP permite descontar productos de inventario y generar un numero
de Orden, el proceso es basico pero permite ver como codifico en Python

La API base es `localhost:8000/api/` esto tambien
esta en la Documentacion de swagger

## Ejecutar la aplicacion con Docker

## Requirementos
- Tener instalado Docker
  
1. Clonar el repositorio con `git clone`
2. Abrir el proyecto con el IDE de su preferencia (vscode, Pycharm)
3. Construir la imagen de Docker con
`docker build -t challenge_3b . `
4. Correr la imagen de Docker con el comando
`docker run -d --name challenge_3b -p 8000:8000 challenge_3b`

## Notas:

Si al detener el Docker y se quiere volver a correr el proyecto
seguramente va mandar un error de que el nombre ya existe 
entonces solo basta con borrar el contendor con  
con `docker rm -f challenge_3b`
y correr nuevamente con
`docker run -d --name challenge_3b -p 8000:8000 challenge_3b`

## Ejecutar las pruebas unitarias
-Correr las pruebas unitarias
`docker exec -it challenge_3b coverage run -m pytest`
## Documentacion de la API con Swagger
`-http://localhost:8000/docs/`
## Ejecutar la aplicacion Sin Docker

## Requirementos

- Tener instalado Python (3.10.12)
- Tener instalado virtualenv

1. Clonar el repositorio con `git clone`
2. Abrir el proyecto con el IDE de su preferencia
3. Instala el entorno virtual en el directorio del proyecto con `pip install virtualenv`
4. Crea un entorno virtual en el directorio del proyecto con `virtualenv venv`
5. Activa el entorno virtual `.\venv\Scripts\activate` y ejecuta 
`pip install -r requirements.txt`

7. Corre las migraciones con `python manage.py migrate`

8. Corre las pruebas unitarias con `coverage run -m pytest`

9. Ejecuta el server de la aplicacion en
`python migrate.py runserver`

10. Ahora estas listo para aceder al API con

`localhost:8000/api/`

## Correr pruebas unitarias con pytest

`coverage run -m pytest`



