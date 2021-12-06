import pandas as pd
from flask import *
import numpy as np

def getPM25():
    url='https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=csv'
    data=pd.read_csv(url)
    return list(data.columns),list(data.values.tolist())




if __name__=='__main__':
    #print(getPM25())
    theads,pm25=getPM25()
    print(pm25)     
   




