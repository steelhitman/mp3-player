from flask import Flask, render_template, request,session, redirect, url_for, escape
app = Flask(__name__)
app.secret_key = "aezakmi"
import serial
import time
import subprocess, sys
import socket
import webbrowser
import serial.tools.list_ports
ip=[]
ip.append(socket.gethostbyname(socket.gethostname()))
print ip
webbrowser.open("http://"+ip[0]+":5000", new=1, autoraise=True)
@app.route('/',methods=['POST','GET'])
def index():
	name="Enrique Iglesias - Heart Attack"
	return render_template('index.html',name=name,ip=ip)

@app.route('/update',methods=['POST','GET'])
def update():
	name="Enrique Iglesias - Heart Attack"
	return render_template('index.html',name=name,ip=ip)

if __name__ == '__main__':
   app.run(host='0.0.0.0')