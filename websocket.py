from flask import Flask
from flask import Blueprint
from flask import request
from flask import Flask, render_template
import main
from flask_socketio import SocketIO, send, emit
import time

#Blueprint('websocket', __name__)

#global socketio
app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect', "/webSigChannel")
def test_connect():
    print ("in connenct")
    emit('my response', {'data': 'Connected'})
  

@socketio.on('connect')
def test_connect():
    print ("in connenct base")
    emit('my response', {'data': 'Connected'})


@socketio.on('message', "/webSigChannel")
def handle_message(message):
    print("vaovao ")
    print('received message: ' + message)
    while 1==1 :
        send("message", "ino begir ")
        time.sleep(1)
        
