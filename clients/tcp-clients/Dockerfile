FROM python:3.8-alpine
WORKDIR /tcp-clients
COPY . .
EXPOSE 65432/tcp
CMD ["python3", "tcpclient.py"]    