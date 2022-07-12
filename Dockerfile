FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install paho-mqtt
RUN pip install board

COPY sensor.py .
COPY sample-config.yml /data/config.yml

RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN apt-get install build-essential python-dev
RUN python3 /app/Adafruit_Python_DHT/setup.py install
RUN rm -r /app/Adafruit_Python_DHT

CMD ["python3", "/app/sensor.py"]