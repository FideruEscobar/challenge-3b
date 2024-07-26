#!/bin/sh

# Ejecutar migraciones
python manage.py migrate

# Iniciar el servidor Django
exec python manage.py runserver 0.0.0.0:${DEFAULT_PORT}