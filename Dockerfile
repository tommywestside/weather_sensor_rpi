FROM python:3.9

WORKDIR /app

RUN apt-get install gcc libc-dev
RUN pip install RPi.GPIO

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY sensor.py .

CMD python sensor.py;