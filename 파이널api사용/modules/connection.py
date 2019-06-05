from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getSoup(api_url):
    try:
        page=urlopen(api_url)
    except HTTPError:
        print("HTTP 에러, 다시시도합니다. 계속생길시 프로그램 강제종료하세요")
        soup=getSoup(api_url)
        return soup
    except URLError:
        print("URL 에러")
    else:
        soup=BeautifulSoup(page.read(),'lxml')
        return soup

def getHtml(api_url):
    try:
        page=urlopen(api_url)
    except HTTPError:
        print("HTTP 에러")
    except URLError:
        print("URL 에러")
    else:
        return page