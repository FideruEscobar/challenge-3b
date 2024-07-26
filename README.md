# challenge-3b
## Author: Luis Fidel Escobar Ambrosio

## Resume

Esta es una API rest creada con Django Rest framework
y como Gestor de Base de datos usa sqllite, por lo tanto
no se necesita conectarse a una base de datos y tampoco
se necesita de algun tipo de aunthenticacion.

La API base es localhost:8000/api/ esto tambien
esta en la Documentacion de swagger

## Ejecutar la aplicacion con Docker

1.-Clonar el repositorio con git clone
2.-Abrir el proyecto con el IDE de su preferencia
3.-Construir la imagen de Docker con 
    docker build -t challenge_3b . 
4.-Correr la imagen de Docker con el comando
    docker run -d --name challenge_3b -p 8000:8000 challenge_3b

## Ejecutar las pruebas unitarias
-Correr las pruebas unitarias
    docker exec -it challenge_3b coverage run -m pytest

## Documentacion de la API con Swagger
-http://localhost:8000/docs/

## Ejecutar la aplicacion Sin Docker

# Requirementos

-Tener instalado Python (3.10.12)
-Tener instalado virtualenv

1.-Clonar el repositorio con git clone
2.-Abrir el proyecto con el IDE de su preferencia
3.-Instala el entorno virtual en el directorio del proyecto

pip install virtualenv

3.-Crea un entorno virtual en el directorio del proyecto con
virtualenv venv

4.-Activa el entorno virtual

.\venv\Scripts\activate

y ejecuta 

pip install -r requirements.txt

6.- Corre las migraciones
python manage.py migrate

7.-Corre las pruebas unitarias

coverage run -m pytest

8. Ejecuta el server de la aplicacion en
python migrate.py runserver

9. Ahora estas listo para aceder al API con

localhost:8000/api/

## Correr pruebas unitarias con pytest

coverage run -m pytest



