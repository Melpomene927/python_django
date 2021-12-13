
import requests
from bs4 import BeautifulSoup

def GetStock():
    url='https://tw.stock.yahoo.com/'
    
    req=requests.get(url)
    if req.status_code == 200:
        soup=BeautifulSoup(req.text,'lxml')
    
    lis=soup.find(id='main-4-HotStock-Proxy').find_all('li')
    datas=[]
    for li in lis:
        data={}
        #print(tbl.find('th').text.strip(),tbl.find('td').text.strip())
        data['股名']=li.find('div', class_="Ta(start)").text.strip()
        data['股價']=li.find('span', class_="Fw(600)").text.strip()
        data['漲跌/漲跌幅']=li.fin()
        datas.append(data)
    

    return datas