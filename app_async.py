import socketio

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
app = socketio.ASGIApp(sio)

# Send an event to the client without receive anything before
# by using start_background_task in connect event
async def task(sid):
  await sio.sleep(2)
  result = await sio.call('numbers', {'numbers': [3, 4]}, to=sid)
  print('task response: ', result)

@sio.event
def connect(sid, environment):
  print(sid, 'connected')

  # Starting background tasks
  sio.start_background_task(task, sid)
  print(sid, 'Background tasks started.')

@sio.event
def disconnect(sid):
  print(sid, 'disconnected')

# Emit an event after sum
@sio.event
async def sum_to_sum_result(sid, data):
  print(sid, data)
  result = data['numbers'][0] + data['numbers'][1]
  await sio.emit('sum_result', { 'result': result }, to=sid)

# Simply return the result after sum
@sio.event
async def sum(sid, data):
  print(sid, data)
  result = data['numbers'][0] + data['numbers'][1]
  return {'result': result}