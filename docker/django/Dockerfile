FROM python:3.10.6-slim
COPY . /golibro
WORKDIR /golibro
RUN apt-get update -y && apt-get install libjpeg-dev libproj-dev gettext libgettextpo-dev netcat -y
RUN pip install pip==23.1.2
RUN pip install -r requirements.txt
