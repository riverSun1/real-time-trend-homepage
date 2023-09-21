# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup
#----------------------------------------------------------------
def humor():
    req = requests.get('https://www.todayhumor.co.kr/')
    soup = BeautifulSoup(req.text, 'html.parser') # html 가져오기
    list_humor = []
    list_humor_href = []
    #------------------------------------------------------------
    for i in soup.find_all("span", attrs={"class": "subject"}):
        list_humor.append(i.text)
        list_humor_href.append("http://www.todayhumor.co.kr/" + i.find("a")["href"])
        # print(i.text)
        # print(list_humor)
    return list_humor, list_humor_href
#----------------------------------------------------------------
def clien():
    req = requests.get('https://www.clien.net/service/')
    soup = BeautifulSoup(req.text, 'html.parser')
    list_clien = []
    list_clien_href = []
    #------------------------------------------------------------
    #for i in soup2.select('#div_content > div.contents_main > div.section_contents.top > div.section_list.recommended > div.section_body > div.list_item > div.list_title > a.list_subject > span.subject'):
    for i in soup.find_all("span", attrs={"data-role": "list-title"}):
        list_clien.append(i.text)
        # print(i.text)
        # print(list_clien)
    for i in soup.find_all("a", class_="list_subject") :
        list_clien_href.append("https://www.clien.net/" + i["href"])   
    return list_clien, list_clien_href
#----------------------------------------------------------------