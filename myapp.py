import flask
from flask import Flask, request
import json
from datetime import datetime
server_port = 5000
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('in.txt', 'a') as file:
        file.write(f'flask.render_template super_ 1303  {datetime.now()}')

    return (f'flask.render_template super_ 1303  {datetime.now()}')

@app.route('/search/', methods=['POST'])
def search():
    error = None
    global count, meteo, s
    s = ''
    count += 1
    qwery = request.get_data()
    meteo = json.loads(qwery)
    for key in meteo:
        s =s + key + '  ' + str(meteo[key]) + '<br>'
    print(s, count, '<br>' )
    return ''

if __name__ == "__main__":
    meteo = ''
    s ='no_data'
    count = 0
    app.run('0.0.0.0',port=server_port)