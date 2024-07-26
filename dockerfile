FROM python:3.10.12-bookworm AS Builder

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt /

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Añadir herramientas necesarias (ajustado a alpine, pero tu imagen base no es alpine)
# Si estás usando una imagen basada en Debian/Ubuntu, usa apt-get en su lugar
RUN apt-get update && apt-get install -y gcc libc-dev && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /code

# Copiar el resto de los archivos del proyecto al contenedor
COPY . .

# Copiar el script de inicio
COPY entrypoint.sh /entrypoint.sh

# Establecer permisos ejecutables para el script de inicio
RUN chmod +x /entrypoint.sh

# Argumento y variable de entorno para el puerto
ARG ARG_DEFAULT_PORT=8000
EXPOSE $ARG_DEFAULT_PORT
ENV DEFAULT_PORT=${ARG_DEFAULT_PORT}

# Usar el script de inicio como ENTRYPOINT
ENTRYPOINT ["/entrypoint.sh"]