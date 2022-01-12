import pandas as pd
import numpy as np

#全域變數
url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=csv'
    
#即時爬取各縣市PM2.5數值
def getPM25(sort='',_ascending='false', _groupby='', _groupbycol=[]):
    data=pd.read_csv(url).dropna()
    ascending = (_ascending == 'true')

    #if (sort !=''):
    #    print(sort)
    #print(f'ascending = {ascending}')

    #抓取所有縣市
    _cities = data.groupby('county').mean().index.tolist()
    _sites =  data.groupby('Site').mean().index.tolist()
    _sortedPM25 = data.sort_values(by='PM25', ascending=False)
    _max = {
        'Site': _sortedPM25['Site'][0],
        'Value': _sortedPM25['PM25'][0],
        'County': _sortedPM25['county'][0]
    }
    _min = {
        'Site': _sortedPM25['Site'].tolist()[-1],
        'Value': _sortedPM25['PM25'].tolist()[-1],
        'County': _sortedPM25['county'].tolist()[-1]
    }

    if (sort !='') & (sort in data.columns):
        print(f'sorted by {sort}, ascending={ascending}')
        data = data.sort_values(by=sort, ascending=ascending)
    

    #表頭
    a = data.columns.tolist()
    #數值
    b = data.values.tolist()
    #其他資訊
    c = {
        'DateTime': data['DataCreationDate'][0], #更新時間
        'Cities': _cities, #所有縣市
        'Sites': _sites, #所有觀測站
        'Max': _max,
        'Min': _min
    }; 

    #進行groupby
    if (_groupby !='') & (_groupby in data.columns):
        if len(_groupbycol)==0:
            #如果沒有指定欄位，就全部輸出
            data = round(data.groupby(_groupby).mean(),2)
        else:
            #有指定欄位
            data = pd.DataFrame([round(data.groupby(_groupby).get_group(col)['PM25'].mean(),2) for col in _groupbycol]
                , index=_groupbycol, columns=['PM25'])
        a = data.index.tolist()
        b = data['PM25'].tolist()
    
    return a,b,c




if __name__=='__main__':
    #print(getPM25())
    theads,pm25,time=getPM25(sort='county', _groupby='county', _groupbycol=['臺北市','臺中市'])
    print(theads,time)     
    for i in pm25:
        print(i)
   




