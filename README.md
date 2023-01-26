# NoAuth

## Descripción
***NoAuth*** se publica como una herramienta bajo licencia GLPv2. Es una herramienta que permite realizar pruebas de penetración basado en la categoría Control de Acceso Roto  de OWASP Top 10, donde el objetivo es comprobar si existen fallas que puedan conducir al acceso, divulgación, modificación y/o destrucción no autorizada de todos los datos sin o fuera de todos los límites del usuario.

## Installing

La forma ideal de realizar la instalación es ingresando los siguientes comandos:

```

pip install -r requirements

```

## Parámetros definidos
- -h: Argumento para desplegar la ayuda.
- -f: Argumento para indicar el nombre del archivo postman collection a procesar.
- -e: Argumento para indicar el nombre del archivo postman environment.
- -t: Argumento para indicar el JWT/TOKEN que se reemplazará en las solicitudes.

## Uso de la herramienta

Puede utilizar el siguiente comando comenzar a emplear NoAuth:

#### 1. Ejecutando desde python:

1.1. Si el archivo postman no contiene variables de ambiente, entonces puede llevar a cabo su ejecución de la siguiente manera.

```
python app.py -f [ruta archivo postman_collection.json]

```

1.2. Si el archivo contiene variables de ambiente, entonces debe añadir el argumento -e, de la siguiente forma:

```
python app.py -f [ruta archivo postman_collection.json] -e [ruta archivo postman_environment.json] 

```

1.3. Si desea realizar solicitudes, utilizando un token de autenticación ingresado a través de argumentos, puede realizar su ejecución de la siguiente forma:

```
python app.py -f [ruta archivo postman_collection.json] -t "[token/ Bearer JWT] -wt [True/False]" 

```

#### Ejemplos de ejecución:

1.1 En caso de validar los endpoint de una API y el "postman_collection" no requiera de "postman_environmet", solo bastaría ingresar el comando de la siguiente forma.

```
python app.py -f "files\API.postman_collection.json" 

```

1.2 Este comando se utilizaría en caso de que se desee validar los endpoints de alguna API, pero el postman_collection requiera de variables de ambiente, en este caso tambien es posible indicar cual es el contenido de dichas variables a través del documento "postman_environment".

```
python app.py -f "files\API.postman_collection.json" -e "files\API.postman_environment.json" 

```
#### NOTA
Para más información, puede verificar todas las funcionalidades ingresando el comando "python app.py -h" y se desplegaran las opciones de ayuda.
