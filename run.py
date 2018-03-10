import os
from flask import Flask
from flask import json
from flask import render_template
from flask import send_from_directory
from flask import request

app = Flask(__name__, template_folder='dist', static_folder='dist/static')

@app.route('/')
def index():
    print(request.remote_addr)

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
