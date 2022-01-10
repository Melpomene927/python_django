import pandas as pd
from flask import *
import numpy as np

def getPM25(sort='',_ascending=False, _groupby=''):
    url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=csv'
    data=pd.read_csv(url)
    #if (sort !=''):
    #    print(sort)
    if (sort !='') & (sort in data.columns):
        print(f'sorted by {sort}, ascending={_ascending}')
        data = data.sort_values(by=sort, ascending=_ascending)
    a = data.columns
    b = data.values.tolist()
    c = data['DataCreationDate'][0];
    if (_groupby !='') & (_groupby in data.columns):
        data = data.groupby(_groupby).mean()
        a = data.index
        b = data['PM25'].tolist()
    
    return list(a),list(b),c




if __name__=='__main__':
    #print(getPM25())
    theads,pm25,time=getPM25(sort='county', _groupby='county')
    print(theads,time)     
    for i in pm25:
        print(i)
   




