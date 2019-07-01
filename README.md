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
    - Client:
        Just run `./client/install.sh`.

    - Server:
        Just run `./server/install.sh`.


# How to launch:

- Client(browser):
    Just run `./client/start.sh`.

- Server(in your server), you can automize the autorun with pm2:
    Just run `./server/start.sh`.

Another way with the standAlone version at `dl.py`.


# Author

- Sanix-darker (Ange SAADJIO).