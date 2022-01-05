
import requests
from bs4 import BeautifulSoup

def GetStock():
    url='https://tw.stock.yahoo.com/world-indices'
    
    req=requests.get(url)
    if req.status_code == 200:
        soup=BeautifulSoup(req.text,'lxml')
    
    lis=soup.find('div', class_='table-body-wrapper').find_all('li')
    datas=[]
    for li in lis:
        data={}
        #print(tbl.find('th').text.strip(),tbl.find('td').text.strip())
        #_divs = li.find_all('div', class_="Fxg(1)")
        data['股名']=li.find('div', class_="Ta(start)").text.strip()
        data['股價']=li.find('span', class_="Fw(600)").text.strip()
        data['漲跌/漲跌幅']= '' #li.find()
        datas.append(data)
    

    return datas

if __name__ == '__main__':
    _datas = GetStock()
    for _data in _datas:
        print(_data)