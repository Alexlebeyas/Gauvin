FROM --platform=linux/amd64 python:3.11-slim-bullseye
COPY . /golibro
WORKDIR /golibro

RUN apt-get update && apt-get install --no-install-recommends -y \
  curl \
  gettext \
  gnupg2 \
  libgettextpo-dev \
  libjpeg-dev \
  libproj-dev \
  netcat

RUN pip install pip==23.1.2
ARG BUILD_ENVIRONMENT=local
RUN pip install -r requirements/${BUILD_ENVIRONMENT}.txt

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install --no-install-recommends -y \
  apt-transport-https \
  make \
  msodbcsql17 \
  mssql-tools \
  unixodbc-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
