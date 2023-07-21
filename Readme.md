
# To create a new project from project-starter, follow these steps:

This project runs on docker, before running it you must have docker and docker compose installed on your local and
follow these steps:

## 1. Clone repo:
git clone git@ssh.dev.azure.com:v3/SpiriaDigital-Canada/Gauvin/Gauvin

## 2. Build docker containers:
Frist, check requirement.txt and then
~~~~
docker-compose build
~~~~
You can build a specific container by specifying the name
~~~~
docker-compose build django
~~~~

## 3. Start containers:
~~~~
docker-compose up
~~~~

### - To list all containers:
~~~~
docker ps
~~~~

### - To connect to a container :
~~~~
docker exec -it container_name bash
Ex: docker exec -it django-golibro bash
~~~~

## 4. Import golibro database :
For the first running you must import golibro database by following these steps

### - Copy a Backup to database container:
You should get a Backup first and copy it at root. Let call it 'golibro.bak'
~~~~
docker cp golibro.bak mssql-golibro:/var/opt/mssql/golibro.bak
~~~~

### - Connect to database container:
~~~~
docker exec -it mssql-golibro bash
~~~~

### - Connect to database terminal and run import command:
~~~~
/opt/mssql-tools/bin/sqlcmd  -U sa -P Password -d master
RESTORE DATABASE [golibro] FROM  DISK = N'/var/opt/mssql/golibro.bak' WITH  FILE = 1,
MOVE N'BDI_Data' TO N'/var/opt/mssql/data/Stagingnew_BDI_Data.mdf',
MOVE N'BDI_Data_log' TO N'/var/opt/mssql/data/Stagingnew_BDI_Data_log.ldf',  NOUNLOAD,  STATS = 5
Go
~~~~
The database import is complete, you can visualize the data with 'Azure Data Studio'
by downloading it from this link https://azure.microsoft.com/en-us/products/data-studio and using
database connection settings.

## 5. After database import, run migrations :
Migrations must run in django container
For the first time you must run migrations with --fake-initial param
~~~~
docker exec -it django-golibro bash
python manage.py migrate --fake-initial
~~~~
Now everything is ready

## To stop all containers :
To stop containers you should be in project directory in your terminal and run
~~~~
docker-compose down
~~~~

## To run linter :
We use Flake8 and Pylint for linter, and .pylintrc as pylint settings and setup.cg as flake8 settings.
Just run this command.
~~~~
docker exec -it django-golibro make lint
~~~~
