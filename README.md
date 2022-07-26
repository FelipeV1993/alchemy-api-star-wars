

## INTRO TO SQL

### To install on Docker (Windows, Linux or Mac)

    $ docker-compose up -d

### Configurar Migrations

Linux o mac:

    $ export FLASK_APP=src/app.py

Windows: 

    $ SET FLASK_APP=src/app.py


### Creamos la carpeta migrations

    $ flask db init

### Crear las migrationes de todos los modelos que estan en el archivo models.py

    $ flask db migrate

### Actualizar la base de datos con todas las migrations

    $ flask db upgrade