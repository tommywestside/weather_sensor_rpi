FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY sensor.py .

COPY sample-config.yml /data/config.yml

CMD python3 /app/sensor.py