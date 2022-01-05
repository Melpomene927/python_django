from flask import *
from datetime import datetime

from werkzeug.exceptions import MethodNotAllowed
#import pandas as pd
#import pandas_datareader as pdr

app = Flask(__name__, static_url_path='/static')
@app.route('/')
@app.route('/index')
@app.route('/index/<string:name>')
def index(name='Mikee'):
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', **locals())

@app.route('/Hello')
def Hello():
    return 'Hello!'

@app.route('/test/<string:name>')
def test(name):
    str=f'Hello world! {name}'
    return str

#呼叫模板網頁
@app.route('/test_html')
def test_html():
    return render_template('test.html')

from stock import GetStock
@app.route('/stock')
def stock():
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stocks=GetStock()
    return render_template('stock.html',**locals())

from pm25 import getPM25
@app.route('/pm25', methods=['GET','POST'])
@app.route('/pm25?sort=<string:sort>', methods=['GET'])
def pm25Site(_sort='',_ascending=False):
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if (request.method == "GET") & (_sort!=''):
        print(f'request.method={request.method} sort by {_sort}')
        theads,pm25=getPM25(sort=_sort)
    elif request.method == "POST":
        _sort = request.form.get('sort')
        print(f'request.method={request.method} sort by {_sort}')
        theads,pm25=getPM25(sort=_sort)
    else:
        theads,pm25=getPM25()
    
    #print(f'method={request.method}')

    return render_template('pm25.html',**locals())

@app.route('/bmi')
def bmiCalc():
    return render_template('bmi.html')

if __name__ == '__main__':
    app.run(debug=True)
