from flask import Flask, jsonify, request
from subprocess import Popen, PIPE, STDOUT
from hashlib import sha256

import _base64

import configparser as ConfigParser

# Configs parameters configParser.get('your-config', 'path1')
configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)

# Secrets parameters
Host = configParser.get('dockerlog-config', 'Host')
Password = configParser.get('dockerlog-config', 'Password')

app = Flask(__name__)
app.config['Secret'] = "Secret"

@app.route('/getlogs', methods=['GET']) # To prevent Cors issues
def index2():
    # Sent in GET requests
    try:
        passord = request.args.get('password')
        container = request.args.get('container')
        
        if sha256(passord.encode()).hexdigest() == Password:
            proc = Popen(['docker', 'logs', str(container)], stdout=PIPE, stderr=STDOUT)
            output = _base64.ENCODE( str(proc.communicate()[0]) )

            # Build the response
            response = jsonify({ 'status':'success', 'message': str(output)[-10000:] })
        else:
            response = jsonify({ 'status':'error', 'message': 'Password not correct!' })

    except:
         response = jsonify({ 'status':'error', 'message': 'Something went Wrong!' })
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response

@app.route('/getcontainers', methods=['GET']) # To prevent Cors issues
def index3():
    # Sent in GET requests
    try:
        passord = request.args.get('password')

        if sha256(passord.encode()).hexdigest() == Password:
            proc = Popen(['docker', 'ps'], stdout=PIPE, stderr=STDOUT)
            output = _base64.ENCODE( str(proc.communicate()[0]) )

            # Build the response
            response = jsonify({ 'status':'success', 'message': str(output)[-10000:] })
        else:
            response = jsonify({ 'status':'error', 'message': 'Password not correct!' })

    except:
         response = jsonify({ 'status':'error', 'message': 'Something went Wrong!' })
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)