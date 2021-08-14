# Python socket.io server project

### From: https://www.youtube.com/watch?v=tHQvTOcx_Ys&ab_channel=MiguelGrinberg

- Activate virtual environment

```bash
. venv/bin/activate
```

- Run the server without websocket enabled

```bash
gunicorn --threads 50 app:app
```

- Run the server with websocket enabled

```bash
gunicorn -k eventlet -w 1 --reload app_name:app
```


## Async server

- Install uvicorn with standard option

```bash
pip3 install "uvicorn[standard]"
```

- Run the server

```bash
uvicorn --reload async_app_name:app
```


## Installation

- Install socketio necessary packages

```bash
pip3 install python-socketio gunicorn eventlet==0.30.2
```

- Install uvicorn with standard option

```bash
pip3 install "uvicorn[standard]"
```


## All requirements:

```
altgraph==0.17
asgiref==3.4.1
bidict==0.21.2
click==8.0.1
dnspython==1.16.0
eventlet==0.30.2
greenlet==1.1.1
gunicorn==20.1.0
h11==0.12.0
httptools==0.2.0
pyinstaller==4.5.1
pyinstaller-hooks-contrib==2021.2
python-dotenv==0.19.0
python-engineio==4.2.1
python-socketio==5.4.0
PyYAML==5.4.1
six==1.16.0
uvicorn==0.14.0
uvloop==0.15.3
watchgod==0.7
websockets==9.1
```
