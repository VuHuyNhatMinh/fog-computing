FROM python:3.8-alpine
WORKDIR /mqtt-clients
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 1883
CMD ["python3", "mqttclient.py"]    