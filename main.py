from flask import *
from datetime import datetime
#import pandas as pd
#import pandas_datareader as pdr

app = Flask(__name__)
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
@app.route('/pm25')
def pm25Site():
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    theads,pm25=getPM25()
    return render_template('pm25.html',**locals())


if __name__ == '__main__':
    app.run(debug=True)
