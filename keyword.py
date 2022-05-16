
from bs4 import BeautifulSoup
import requests

def area(search):
    url_list = []
    for page_num in range(1, 5):
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page_num)
        url_list.append(url)

    # ConnectionError방지
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75"}

    news_title = []
    news_url = []
    contents = []

    for url in url_list:
        # html불러오기
        original_html = requests.get(url, headers=headers)
        html = BeautifulSoup(original_html.text, "html.parser")

        # 검색결과
        articles = html.select("div.group_news > ul.list_news > li div.news_area > a")

        # 뉴스기사 제목 가져오기
        for i in articles:
            news_title.append(i.attrs['title'])

        # 뉴스기사 URL 가져오기
        for i in articles:
            news_url.append(i.attrs['href'])

        # 뉴스기사 내용 크롤링하기
        for i in news_url:
            # 각 기사 html get하기
            news = requests.get(i, headers=headers)
            news_html = BeautifulSoup(news.text, "html.parser")
            # 기사 내용 가져오기 (p태그의 내용 모두 가져오기)
            contents.append(news_html.find_all('p'))

    return news_title,news_url,contents



print(area('제주'))