import requests
from bs4 import BeautifulSoup

def get_href(soup):
    result=[]

    div=soup.find("div",class_="list_body newsflash_body")

    for dt in div.find_all("dt",class_="photo"):
        result.append(dt.find("a")["href"])

    return result

def get_requser(section):
    custom_header={
        'referer':'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url="https://news.naver.com/main/list.nhn"

    sections={
        "정치" : 100,
        "경제" : 101,
        "사회" : 102,
        "생활" : 103,
        "세계" : 104,
        "과학" : 105
    }

    req=requests.get(url,headers=custom_header,
                     params={"sid1":sections[section]})

    return req

def main():
    list_href=[]

    section=input('정치,경제,사회,생활,세계,과학 중 선택')

    req=get_requser(section)
    soup=BeautifulSoup(req.text,"html.parser")

    list_href=get_href(soup)

    print(list_href)

if __name__=="__main__":
    main()
