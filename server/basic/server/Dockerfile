FROM python:3.8-alpine
WORKDIR /server
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# CMD ["python3", "main.py"]
# CMD ["chmod", "+x", "./wait-for" ]