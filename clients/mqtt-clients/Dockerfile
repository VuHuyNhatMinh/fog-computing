FROM python:3.8-alpine
WORKDIR /mqtt-clients
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "mqttclient.py"]    