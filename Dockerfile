FROM python:3.9

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install paho-mqtt
RUN pip3 install board
RUN pip3 install Adafruit_Python_DHT

COPY sensor.py .
COPY sample-config.yml /data/config.yml

CMD ["python3", "/app/sensor.py"]