
import requests
from bs4 import BeautifulSoup

def GetStock():
    url='https://tw.stock.yahoo.com/'
    
    req=requests.get(url)
    if req.status_code == 200:
        soup=BeautifulSoup(req.text,'lxml')
    
    tables=soup.find(id='ystkchatwtb-table-tab1').find_all('table')
    datas=[]
    for tbl in tables:
        data={}
        #print(tbl.find('th').text.strip(),tbl.find('td').text.strip())
        data['分類']=tbl.find('th').text.strip()
        data['指數']=tbl.find('td').text.strip()
        datas.append(data)
    

    return datas