<img src="./client/static/logoo.png">

# DockerLogs

An Experimental way to get Logs of any of your application running with docker on a server directly on a browser client application.

# Features

- Get all running containers at the server(ID, names, etc...).
- Get all logs from a docker container(in realtime) with a client app(browser).

# How it's works

There must be one instance running locally, the principe is that, ngrock will open a dor to access a computer of one developper and then the client there will send requests directly to the server.

# Installation

- First you need to rename example.config.txt to config.txt and asl the Author for extras elements.

- Second: Make sure to configure the ServerIp/Host for the client and the server by renaming example.config.txt to config.txt

- Third:
    - For Client, run `cd client && pip install -r requirements.txt && sh ./install.sh`.

    - For the Server, you just need to run `cd client && pip install -r requirements.txt && sh ./install.sh`.


# How to launch:

- Client(browser):
    Just run `cd client && sh ./start.sh`, the client app is running on `http://127.0.0.1:7974`

- Server(in your server), you can automatize the auto-run with pm2, the app will running on server at `http://127.0.0.1:5000`:
    Just run `cd server && sh ./dockerLog.sh.sh`.

Another way with the standAlone version is to hit `python dl.py`.

# Author

- Sanix-darker (Ange SAADJIO).