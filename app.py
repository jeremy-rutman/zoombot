from flask import Flask, redirect
from flask import render_template
import time

do_this_file = 'commands.txt'

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
    htmlfile = 'templates/json.html'
    htmlfile2 = 'templates/json2.html'
#     with open(htmlfile, 'a') as fp:
# #        lines = fp.readlines()
#         fp.write('fwd\n')
#         fp.flush()
#     render_template('json.html')
# #    return redirect(url_for('json.html'))
#     return redirect('json.html')
    with open(do_this_file,'a+') as fp:
        fp.write('FWD\t'+str(time.time())+'\n')
    return render_template('json.html')

@app.route('/backward')
def backward():
    print("BACKWARD")
    return render_template('json.html')

@app.route('/left')
def left():
    print("LEFT")
    return("nothing")

@app.route('/right')
def right():
    print("RIGHT")
    return("nothing")

@app.route('/')
def home():
   return render_template('json.html')
if __name__ == '__main__':
   app.run()
