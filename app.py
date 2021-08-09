import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environment):
  print(sid, 'connected')

@sio.event
def disconnect(sid):
  print(sid, 'disconnected')

@sio.event
def sum(sid, data):
  print(sid, data)
  result = data['numbers'][0] + data['numbers'][1]
  sio.emit('sum_result', { 'result': result }, to=sid)