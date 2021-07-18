import requests
import base64

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

def sendfile(fname):
    url = 'http://127.0.0.1:5000/instructions'
    resp = requests.get(url)

    print('response is ',resp)
    print('response content',resp.json())
    print('response content',resp.json())
    return resp


print(sendfile('backproj7.jpg'))