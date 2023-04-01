FROM python:3.8-alpine
WORKDIR /tcp-clients
COPY . .
EXPOSE 65432/TCP
CMD ["python3", "tcpclient.py"]    