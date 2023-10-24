import os
import time
import requests
import random
from Compression import Compress

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
folderName = '/Contents'
# Developed url
url = 'http://localhost:8080/api/data'

# Deployed url
# url = 'http://44.203.145.174:8080/api/data'
headers = {'Accept': 'application/json',
           'Content-Type': 'application/json'}

def createMessage(path, file):
    msg = {}

    fileName, fileType = os.path.splitext(file)
    msg['fileType'] = fileType[1:]

    fileSize = os.path.getsize(path)
    msg['fileSize'] = int(fileSize)

    file = open(path, 'rb')
    content = file.read()
    compress = Compress(content)
    num = random.randint(0, 4)
    if num == 0:
        content_compressed = content
        msg['fileName'] = fileName
    elif num == 1:
        content_compressed = compress.deflate()
        msg['fileName'] = fileName + '.deflate'
    elif num == 2:
        content_compressed = compress.lzma()
        msg['fileName'] = fileName + '.lzma'
    elif num == 3:
        content_compressed = compress.lz4()
        msg['fileName'] = fileName + '.lz4'        
    elif num == 4: 
        content_compressed = compress.BZip2()
        msg['fileName'] = fileName + '.bz2'   
    content = str(content_compressed)
    msg['contentStr'] = content

    msg['timeSent'] = time.time() * 10e3

    return msg

def main():
    PATH = BASE_PATH + folderName
    files = os.listdir(PATH)
    while True:
        for file in files:
            path = PATH + '/' + file
            payload = createMessage(path, file)
            response = requests.post(url, json=payload, headers=headers)

if __name__ == '__main__':
    main()