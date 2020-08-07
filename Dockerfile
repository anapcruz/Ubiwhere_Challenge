FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get -y update && apt-get install gdal-bin -y
#RUN apt-get -y update && apt-get install gdal-bin postgresql-client postgresql -y
#RUN pg_ctlcluster 11 main start
#RUN apt-get install binutils libproj-dev gdal-bin -y
#RUN createdb django_restframework_gis
#RUN psql -U postgres -h db -d django_restframework_gis -c "CREATE EXTENSION postgis"

COPY . /code/

