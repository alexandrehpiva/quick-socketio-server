# Python socket.io server project

### From: https://www.youtube.com/watch?v=tHQvTOcx_Ys&ab_channel=MiguelGrinberg

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