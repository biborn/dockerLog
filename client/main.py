# coding: utf-8
from flask import Flask, jsonify, request, render_template
# importing the requests library 
import requests
import _base64
import configparser as ConfigParser
import json
import os

from threading import Thread

# Configs parameters configParser.get('your-config', 'path1')
configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)

# Secrets parameters
Host = configParser.get('dockerlog-config', 'Host')
Password = configParser.get('dockerlog-config', 'Password')

# api-endpoint 
URL = Host

app = Flask(__name__)
app.config['Secret'] = "Secret"

@app.route('/', methods=['GET']) # To prevent Cors issues
def index():
    # # Sent in GET requests
    # param = request.args.get('param')

    #  # Emission de la requette au serveur avec le port ouver 5000

    # # Build the response
    # response = jsonify({ 'status':'success', 'message': 'Welcome to dockerLog API.' })
    # # Let's allow all Origin requests
    # response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return render_template("index.html")


@app.route('/getall', methods=['GET']) # To prevent Cors issues
def index2():
    # Sent in GET requests
    try:
        # sending get request and saving the response as response object 
        r = requests.get(url = URL+"/getcontainers?password="+Password) 
        jsonMessage = json.loads(str(r.content).replace("\\n", "").replace("b'", "").replace("'", ""))
    
        # Build the response
        response = jsonify({ 'status':'success', 'message': _base64.DECODE(jsonMessage['message'])[-10000:] })
    except:
        response = jsonify({ 'status':'error', 'message': 'Something went Wrong!' })

    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response


@app.route('/logs', methods=['GET']) # To prevent Cors issues
def index3():
    try:
        # Sent in GET requests
        container = request.args.get('container')
        # sending get request and saving the response as response object 
        r = requests.get(url = URL+"/getlogs?container="+str(container)+"&password="+Password) 
        jsonMessage = json.loads(str(r.content).replace("\\n", "").replace("b'", "").replace("'", ""))
    
        # Build the response
        response = jsonify({ 'status':'success', 'message': _base64.DECODE(jsonMessage['message'])[-10000:] })
    except:
        response = jsonify({ 'status':'error', 'message': 'Something went Wrong!' })

    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response


def ngrok_process():
    print("Starting ngrok...")
    os.system("./ngrok http 7974")

# Endpoint to list containers

# Endpoint to get logs

if __name__ == "__main__":
    # Starting the ngrok thread
    Thread(target = ngrok_process).start()


    # Starting the app
    app.run(host='0.0.0.0', debug=True, port=7974)
