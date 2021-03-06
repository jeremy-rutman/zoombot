# to run this do
# FLASK_APP=app.py flask run


from flask import Flask, redirect
from flask import render_template
import time

from flask import json
from flask import jsonify

do_this_file = 'commands.txt'
max_lines_in_file = 5
min_lines_in_file = 1
app = Flask(__name__)
#rendering the HTML page which has the button
@app.route('/json')


def json():
    print('doing json thing')
#    return render_template('/home/jeremy/Dropbox/projects/PycharmProjects/zoombot/json.html')
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/forward')
def forward():
    print("FORWARD")
    with open(do_this_file,'a+') as fp:
        fp.write('F\t'+str(round(time.time(),2))+'\n')
    return render_template('json.html')

@app.route('/backward')
def backward():
    print("BACKWARD")
    with open(do_this_file,'a+') as fp:
        fp.write('B\t'+str(round(time.time(),2))+'\n')
    return render_template('json.html')

@app.route('/left')
def left():
    print("LEFT")
    with open(do_this_file,'a+') as fp:
        fp.write('L\t'+str(round(time.time(),2))+'\n')
    return("nothing")

@app.route('/right')
def right():
    print("RIGHT")
    with open(do_this_file,'a+') as fp:
        fp.write('R\t'+str(round(time.time(),2))+'\n')
    return("nothing")


@app.route('/instructions')
def instructions():
    print("send instructions")
    with open(do_this_file,'r') as fp:
        lines = fp.readlines()
        #data = {i:l  for i,l in enumerate(lines)}
        data = {float(l.split('\t')[1].replace('\n','')):l.split('\t')[0] for l in lines}
#        print(f'lines: {lines}')
#        print(f'data {data}')
        fp.close()
    if len(lines) > max_lines_in_file:
        latest_lines = lines[-min_lines_in_file:]
        with open(do_this_file,'w') as fp:
            fp.writelines(latest_lines)
    return data

@app.route('/')
def home():
   return render_template('json.html')

if __name__ == '__main__':
    instructions()
    app.run()

instructions()