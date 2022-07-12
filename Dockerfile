FROM python:3.9-alpine

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN python -m pip install --upgrade pip
RUN pip install RPi.GPIO

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY sensor.py .

CMD python /app/sensor.py