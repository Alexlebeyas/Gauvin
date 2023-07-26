FROM python:3.10.6-slim
COPY . /golibro
WORKDIR /golibro
RUN apt-get update -y && apt-get install libjpeg-dev libproj-dev gettext libgettextpo-dev netcat -y

RUN pip install pip==23.1.2
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

RUN apt-get update
RUN apt-get install -y curl apt-transport-https
RUN apt-get update && apt-get install -y gnupg2
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get install make
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools unixodbc-dev
