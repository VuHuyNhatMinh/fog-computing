FROM python:3.8-alpine
WORKDIR /udp-clients
COPY . .
EXPOSE 65432/udp
CMD ["python3", "udpclient.py"]    