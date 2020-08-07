FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get -y update && apt-get install gdal-bin -y
#RUN apt-get install binutils libproj-dev gdal-bin -y
COPY . /code/

