import socketio

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
app = socketio.ASGIApp(sio)

@sio.event
def connect(sid, environment):
  print(sid, 'connected')

@sio.event
def disconnect(sid):
  print(sid, 'disconnected')

@sio.event
async def sum(sid, data):
  print(sid, data)
  result = data['numbers'][0] + data['numbers'][1]
  await sio.emit('sum_result', { 'result': result }, to=sid)