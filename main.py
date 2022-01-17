from flask import *
from datetime import datetime
from werkzeug.exceptions import MethodNotAllowed 
import json

### 生成app物件
app = Flask(__name__, static_url_path='/static')

### 首頁Route
@app.route('/')
@app.route('/index')
@app.route('/index/<string:name>')
def index(name=''):
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    showName = 'd-none' if name == '' else ''
    return render_template('index.html', **locals())

########################################
#=====  RestAPI測試 ======
@app.route('/Hello')
def Hello():
    return 'Hello!'

@app.route('/test/<string:name>')
def test(name):
    str=f'Hello world! {name}'
    return str



########################################
############# 呼叫模板網頁 ##############
########################################

########################################
#- 我愛運動
@app.route('/test_html')
def test_html():
    return render_template('test.html')

########################################
#- 股票爬蟲
from stock import GetStock
@app.route('/stock')
def stock():
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stocks=GetStock()
    return render_template('stock.html',**locals())

########################################
#- PM2.5即時資料
from pm25 import getPM25
@app.route('/pm25', methods=['GET','POST'])
@app.route('/pm25/sort=<string:sort>', methods=['GET'])
@app.route('/pm25/ascending=<string:ascending>', methods=['GET'])
@app.route('/pm25/sort=<string:sort>&ascending=<string:ascending>', methods=['GET'])
def pm25Site(sort='',ascending='false'):
    #目前時間
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    extra={}
    #變數取得
    if request.method == "POST":
        sort = request.form.get('sort')
        ascending = request.form.get('ascending') 
    print(f'request.method={request.method} sort by {sort}, ascending={ascending}') 
    if sort == '':
        theads,pm25,extra=getPM25(_ascending=ascending)
    else:
        theads,pm25,extra=getPM25(sort=sort, _ascending=ascending) 

    time = extra['DateTime']
    ascending = str(not(ascending == 'true')).lower()
    return render_template('pm25.html',**locals())

########################################
#- PM2.5視覺化, 使用Apache Echarts的Javascript模組
@app.route('/pm25-charts', methods=['GET','POST'])
def pm25Charts():
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    _date=datetime.now().strftime('%Y-%m-%d')

    return render_template('pm25charts.html',**locals())

########################################
#- PM2.5數據取得,供Call-back使用
@app.route('/pm25-data/groupby=<groupby>', methods=['GET'])
@app.route('/pm25-data', methods=['GET','POST'])
def pm25datas(groupby=''):
    extra={}
    if request.method == "POST":
        groupby = request.form.get('groupby')
    
    if groupby != "":
        print(f'groupby={groupby}')
        theads,pm25,extra=getPM25(_groupby=groupby)
    else:
        theads,pm25,extra=getPM25()

    time = extra['DateTime']
    #print(theads)
    #print(pm25)
    #print(extra)
    return json.dumps({"columns":theads, "datas":pm25, "extra": extra}, ensure_ascii=False)

########################################
#- BMI計算機
@app.route('/bmi')
def bmiCalc():
    return render_template('bmi.html')


########################################

#啟動網站
if __name__ == '__main__':
    app.run(debug=True)
