# NoAuth

## Descripción
***NoAuth*** se publica como una herramienta bajo licencia GLPv2. Es una herramienta que permite realizar pruebas de penetración basado en la categoría Control de Acceso Roto  de OWASP Top 10, donde el objetivo es comprobar si existen fallas que puedan conducir al acceso, divulgación, modificación y/o destrucción no autorizada de todos los datos sin o fuera de todos los límites del usuario.

## Installing

La forma ideal de realizar la instalación es ingresando los siguientes comandos::

```

pip install -r requirements

```

## Uso de la herramienta

Puede utilizar el siguiente comando comenzar a emplear NoAuth:

```
1. Ejecutando python:

1.1 Si el archivo postman no contiene variables de ambiente, entonces puede llevar a cabo su ejecución de la siguiente manera.

python app.py -f [ruta archivo postman_collection.json]

1.2 Si el archivo contiene variables de ambiente, entonces debe añadir el argumento -e, de la siguiente forma:

python app.py -f [ruta archivo postman_collection.json] -e [ruta archivo postman_environment.json] 

```
