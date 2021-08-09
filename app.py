import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environment):
  print(sid, 'connected')

@sio.event
def disconnect(sid):
  print(sid, 'disconnected')