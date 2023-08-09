
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
docker compose up -d
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
docker compose down
~~~~

## To run linter :
We use Flake8 and Pylint for the linter. .pylintrc and setup.cg
files are used for pylint and flake8 parameters respectively.
Just run this command.
~~~~
docker exec -it django-golibro make lint
~~~~

## Formating
We recommand to install Black in your IDE. In Pycharm just install https://plugins.jetbrains.com/plugin/14321-blackconnect
and run alt+shift+B to format
or go to settings > tools >  backconnect and allow format on saving
Do not forget to set line length to 120

## To run test :
Please make sure test passes before any commits
~~~~
docker exec -it django-golibro python manage.py test
~~~~

##box tool
A small executable file was build to give you docker shortcuts. ./box --help to get the details

# Infrastructure

## Terraform

1. Install Terraform and the Azure CLI tool

1. Ask the client to invite you to their Azure Portal account with at least `contributor` access

```
az login # Login with Spira credentials
az account set --subscription "e3316aac-532c-4f26-9feb-4703dd5ce879"

cd terraform

# This project uses Terraform workspaces

# QA environment
terraform workspace select qa
terraform plan -var-file=qa.tfvars
terraform apply -var-file=qa.tfvars

# UAT environment
terraform workspace select uat
terraform plan -var-file=uat.tfvars
terraform apply -var-file=uat.tfvars

# Production environment
terraform workspace select prod
terraform plan -var-file=prod.tfvars
terraform apply -var-file=prod.tfvars
```

### Variables

Default values for suitable for non-prod environments are set in `variables.tf`. These can be overridden for QA/UAT envs where it makes sense, and *should* be overriden with production suitable valuues in the production environment.

See:
- variables.tf
- terraform.tfvars
- qa.tfvars
- uat.tfvars
- prod.tfvars

## Secret Values

Non-secret values should be checked into source code and managed with Django configuration.

The environment specific key-vault is created via Terraform, but secret values are managed outside Terraform, and are referenced as secrets and environment variables in the container apps.

After creating a secret, you'll need to add the data attribute, and secret and environment variable definitions to the relevant container apps, and run `terraform apply -var-file=ENV.tfvars` for the specific environment.

After updating a secret, you'll need to run `terraform apply -var-file=ENV.tfvars` for the specific environment.

User access to the key vaults is managed by the `key_vault_access_policies` Terraform variable.

## SMTP

There is an Azure marketplace Sendgrid account in the production resource group `gauvin-rg-prod`.

It is meant for use in all environments. It can be accessed [here](https://portal.azure.com/#@impgauvin.onmicrosoft.com/resource/subscriptions/e3316aac-532c-4f26-9feb-4703dd5ce879/resourceGroups/gauvin-rg-prod/providers/Microsoft.SaaS/resources/gauvin-sendgrid/overview).
