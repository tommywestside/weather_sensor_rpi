FROM python:3.9-alpine

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install RPi.GPIO

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY sensor.py .

ENTRYPOINT ["python3 /app/sensor.py"]