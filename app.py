import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

# Send an event to the client without receive anything before
# by using start_background_task in connect event
def task(sid):
  sio.sleep(2)
  result = sio.call('numbers', {'numbers': [3, 4]}, to=sid)
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
def sum_to_sum_result(sid, data):
  print(sid, data)
  result = data['numbers'][0] + data['numbers'][1]
  sio.emit('sum_result', { 'result': result }, to=sid)

# Simply return the result after sum
@sio.event
def sum(sid, data):
  print(sid, data)
  result = data['numbers'][0] + data['numbers'][1]
  return {'result': result}