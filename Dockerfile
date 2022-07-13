FROM python:3.9

RUN apt-get install gcc libc-dev
RUN pip install RPi.GPIO

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY sensor.py .

CMD python /app/sensor.py;