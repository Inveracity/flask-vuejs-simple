import os
from flask import Flask
from flask import json
from flask import render_template
from flask import send_from_directory
from flask import request

app = Flask(__name__, template_folder='dist', static_folder='dist/static')

@app.route('/')
def index():
    print request.remote_addr

    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'dist/static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/api/myip')
def myip():


    response = app.response_class(
        response=json.dumps(
            {
                'myip': request.remote_addr
            }
        ),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/<path:invalid>')
def page_not_found(*args, **kwargs):

    response = app.response_class(
        response=json.dumps(
            {
                'error': 'not found'
            }
        ),
        status=404,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)


'''
# Written by Christopher Baklid
# This code can open a port on the Sagem F@st 3666 home router without having to log in.
# The first request creates a new table entry
# The second request inputs the ports and ip addresses and the stuff we need

import requests
url = 'http://192.168.0.1/goform/RgForwarding'

precursor = {
    'PortForwardingCreateRemove'  : '1',
    'PortForwardingTable'         : '0',
}

payload = {
    'PortForwardingCreateRemove'  : '0',
    'PortForwardingLocalIp'       : '192.168.0.3',
    'PortForwardingLocalStartPort': '8081',
    'PortForwardingLocalEndPort'  : '8081',
    'PortForwardingExtStartPort'  : '8081',
    'PortForwardingExtEndPort'    : '8081',
    'PortForwardingProtocol'      : '254',
    'PortForwardingDesc'          : 'sessorium',
    'PortForwardingEnabled'       : '1',
    'PortForwardingApply'         : '2',
    'PortForwardingTable'         : '0',
}

headers = {'Content-Type':'application/x-www-form-urlencoded'}
r = requests.post(url, data=precursor, headers=headers)
r = requests.post(url, data=payload, headers=headers)
print r.text
'''