import requests
import base64
from time import sleep

#for security key
# from flask import Flask, request, jsonify, make_response
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# import uuid
# import jwt
# import datetime
# from functools import wraps


# url = 'http://54.74.156.144:80/predict'
# resp = requests.post(url,files={"file": open(fname,'rb')})
# print('response is ',resp)
# print('response content',resp.json())

def get():
#    url = 'http://127.0.0.1:5000/instructions'
    url = 'http://178.128.26.70:5000/instructions'
    resp = requests.get(url)
    content = resp.content
    try:
        data = eval(content)
    except:
        data = {}
    return data


# while(1):
#     get()
#     sleep(0.1)
