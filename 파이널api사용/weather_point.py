from modules import connection as cn ,apiurl as au
from modules.dataprocess import DataProcess
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import date
import sys
import math

def main(start_date,end_date):
    api_url=au.weather_point_url(start_date,end_date)
    dp=DataProcess()
    data=[]
    delta= date(int(end_date[:4]), int(end_date[4:6]), int(end_date[6:8])) -date(int(start_date[:4]), int(start_date[4:6]), int(start_date[6:8]))
    for itr in range(math.ceil(delta.days/10)):
        soup=cn.getSoup(api_url+str(itr+1))
    #item 안의 모든 자식을 해당 자식의 name:text 형태로 딕셔러니를 만든다
    #item 한개당 한개의 자식 딕셔너리 리스트를 원소로하는 리스트를 만들고
    #모든 item리스를 모아 data에저장한다.
    #data=[ {ele.name:ele.text.split(" ")[0]} for item in soup.find_all("item") for ele in item ]
        if isinstance(soup,BeautifulSoup):
            for item in soup.find_all("info"):
                row={}
                for ele in item:
                    if isinstance(ele,Tag):
                        row.update({ele.name:ele.string.split(" ")[0]})
                data.append(row)
    if len(data)!=0:
        dp.setDataList(data)
    else:
        print("no data to fetch!")
    dp.writeToCsv("천안 종관기상FROM="+start_date+"END="+end_date+" ")

if __name__=="__main__":
    if len(sys.argv)==3:
        main(sys.argv[1],sys.argv[2])
    else :
        print("input format: firstdateofyear  enddateofyear")