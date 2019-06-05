from modules import connection as cn ,apiurl as au
from modules.dataprocess import DataProcess
from bs4 import BeautifulSoup
import math
import sys

def main(start_date,end_date,area,crop):
    api_url=au.crop_weather_url(start_date,end_date,area,crop)
    soup=cn.getSoup(api_url+"1")
    dp=DataProcess()
    totalcount=int(soup.find("totalcount").text)
    numofrows=int(soup.find("numofrows").text)
    pageMaxNum=math.ceil(totalcount/numofrows)
    data=[]
    for itr in range(pageMaxNum):
        soup=cn.getSoup(api_url+str(itr+1))
    #item 안의 모든 자식을 해당 자식의 name:text 형태로 딕셔러니를 만든다
    #item 한개당 한개의 자식 딕셔너리 리스트를 원소로하는 리스트를 만들고
    #모든 item리스를 모아 data에저장한다.
    #data=[ {ele.name:ele.text.split(" ")[0]} for item in soup.find_all("item") for ele in item ]
        for item in soup.find_all("item"):
            row={}
            for ele in item:
                row.update({ele.name:ele.text.split(" ")[0]})
            data.append(row)
    if len(data)!=0:
        dp.setDataList(data)
    else:
        print("no data to fetch!")
    dp.writeToCsv("AREA-"+area+"CROP-"+crop+"FROM-"+start_date+"END-"+end_date+" ")

if __name__=='__main__':
    if len(sys.argv)==5:
        main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    else : 
        print("input form:startdate  enddate  city  crop")