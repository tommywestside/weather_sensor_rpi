FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install paho-mqtt
RUN pip install board
RUN pip install adafruit_dht

COPY sensor.py .
COPY sample-config.yml /data/config.yml

CMD ["python3", "/app/sensor.py"]