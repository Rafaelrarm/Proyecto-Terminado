# Proyecto-final realizado por Rafael y Quimey

CASOS DE PRUEBAS LINK A DRIVE: 

https://docs.google.com/spreadsheets/d/1B4moB1th5H5-ERMqw-d-5GLGdp-X6TYH/edit?usp=sharing&ouid=106955430778422038598&rtpof=true&sd=true


Entrega final de CoderHouse python, este codigo contiene:

-Vistas
-Formularios
-Modelos
-Templates

# Instalar

Para instalar este software, debe hacer:

## Comprobar la versión de python 
Este proyecto se escribió con python 3.9.12, por lo que le sugiero que pruebe con esta versión o superior para no tener problemas de compatibilidad.

Cómo verifico mi versión de python, 

En *nix systems:

> python --version
> Python 3.9.12 

En windows:

c:\> py --version
c:\> Python 3.8.0

## Instalar dependencias

Para instalar dependencias necesitas ejecutar pip install, asegúrate de estar en la carpeta del proyecto y puedes ver el archivo requirements.txt cuando haces ls o dir:

> pip install -r requirements.txt

Este último devolverá un montón de cosas en la terminal.

Algunos sistemas operativos requerirán que uses pip3 en lugar de pip

## Configuración de la aplicación Django

Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django.

### Migraciones

Inicializar la base de datos
*nix:
> python manage.py migrar

windows:
c:\> py mananage.py migrate


### Ejecutar el servidor de prueba

> python mananage.py runserver

windows:
c:\> py manage.py runserver

Ir a localhost:8000/

para tener acceso a la aplicación.

Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.