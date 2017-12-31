from flask import Flask,  render_template
from flask import Blueprint
from flask import request
from flask_sse import sse
from channel import channel
from flask_socketio import SocketIO, send, emit
import time

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')
app.register_blueprint(channel, url_prefix='/channel')

print("started")


@app.route("/")
def page():
    return render_template("login.html")

@app.route("/main/<username>")
def main_page(username):
	return render_template("main2.html", name=username)


@app.route("/wait/<Cid>")
def wait_page(Cid):
	return render_template("wait.html", name=Cid)



@app.route("/join/<Cid>")
def join_page(Cid):
	return render_template("join.html", name=Cid)

@app.route("/room/<Cid>/<IsHost>")
def join_room(Cid, IsHost):
    return render_template("room.html", name=Cid, isHost=IsHost)
# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)

# @app.route("/", methods=['POST'])
# def hello():
# 	print "Hello World!"
# 	print "req:  ", request.data
# 	sse.publish({"message": "Hello!"}, type='greeting')
# 	return "resssponsee main"

socketio = SocketIO(app)

@socketio.on('connect', "/webSigChannel")
def test_connect():
    send("rom server ")
    print ("in connenct")
    emit('my response', {'data': 'Connected'})
  
@socketio.on("message", "/webSigChannel")
def get_message(msg):
	print ("msg is :", msg)

@socketio.on("sdp", "/webSigChannel")
def get_message(json):
	print ("msg is :", json)
	emit("sdp", json, broadcast=True)

@socketio.on("ice", "/webSigChannel")
def get_message(json):
	print ("msg is :", json)
	emit("ice", json, broadcast=True)