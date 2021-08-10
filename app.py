import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

# Callback to be executed on receive task response
def task_callback(result):
  print('task response: ', result)

# Send an event to the client without receive anything before
# by using start_background_task in connect event
def task(sid):
  sio.sleep(2)
  sio.emit('numbers', {'numbers': [3, 4]}, callback=task_callback)

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