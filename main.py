from flask import *
from datetime import datetime

from werkzeug.exceptions import MethodNotAllowed
#import pandas as pd
#import pandas_datareader as pdr
import json

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
@app.route('/pm25/sort=<string:sort>', methods=['GET'])
@app.route('/pm25/ascending=<string:ascending>', methods=['GET'])
@app.route('/pm25/sort=<string:sort>&ascending=<string:ascending>', methods=['GET'])
def pm25Site(sort='',ascending='false'):
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if request.method == "POST":
        sort = request.form.get('sort')
        ascending = request.form.get('ascending')
    
    #ascending = str(ascending).lower()
    print(f'request.method={request.method} sort by {sort}, ascending={ascending}')

    if sort == '':
        theads,pm25,time=getPM25(_ascending=ascending)
    else:
        theads,pm25,time=getPM25(sort=sort, _ascending=ascending)

    #print(f'method={request.method}')

    return render_template('pm25.html',**locals())

@app.route('/pm25-charts')
def pm25Charts():
    return render_template('pm25charts.html',**locals())

@app.route('/pm25-data/groupby=<groupby>', methods=['GET'])
@app.route('/pm25-data', methods=['GET','POST'])
def pm25datas(groupby=''):
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        groupby = request.form.get('groupby')

    if groupby != "":
        theads,pm25,time=getPM25(_groupby=groupby)
    else:
        theads,pm25,time=getPM25()
    return json.dumps({"columns":theads, "datas":pm25, "time": time}, ensure_ascii=False)

@app.route('/bmi')
def bmiCalc():
    return render_template('bmi.html')

if __name__ == '__main__':
    app.run(debug=True)
