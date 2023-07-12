
# Docker setup

1. rename .env.example in .env and adjust accordinly
1. go to the root of the project
1. build containers `docker compose build`
1. Start containers `docker compose up`
1. Run migrations\
    1. First, open a new terminal while the project is running in the main terminal\
    1. `docker exec -it django-golibro bash` or adjust according to the django container name
    1. `python manage.py makemigrations`
    1. `python manage.py migrate`
1. Create superuser\
It could help to access the administration interface or to connect for the tests\
When asked for an email address, enter any valid value, but remember it as it will be useful later\
`docker exec -it xxxxxxx-web-1 bash`\
`python manage.py createsuperuser`
1. To stop all containers:
`docker compose down`
~~~~

# DB initialization

from https://learn.microsoft.com/en-us/azure/azure-sql-edge/backup-restore

- get a Back up and copy it at root. Let call it 'golibro.bak'
- copy file into container \
`docker cp golibro.bak mssql-golibro:/var/opt/mssql/golibro.bak`

- then from  Azure Data Studio (https://azure.microsoft.com/en-us/products/data-studio)\
`
USE [master]
RESTORE DATABASE [golibro] FROM  DISK = N'/var/opt/mssql/golibro.bak' WITH  FILE = 1,
MOVE N'BDI_Data' TO N'/var/opt/mssql/data/Stagingnew_BDI_Data.mdf',
MOVE N'BDI_Data_log' TO N'/var/opt/mssql/data/Stagingnew_BDI_Data_log.ldf',  NOUNLOAD,  STATS = 5`


