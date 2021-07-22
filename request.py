import requests
import base64
from time import sleep

def get():
#    url = 'http://127.0.0.1:5000/instructions'
    url = 'http://178.128.26.70:5000/instructions'
    resp = requests.get(url)
    content = resp.content
    try:
        data = eval(content)
        data = {float(k):v for k,v in data.items()}
    except Exception as e:
        print(e)
        data = {}
    return data


if __name__ == '__main__':
    while(1):
        data = get()
        print(data)
        sleep(0.1)
