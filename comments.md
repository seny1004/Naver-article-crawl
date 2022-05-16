# Naver-article-crawl







from selenium import webdriver
import time
import pandas as pd


def get_naver_news_comments(url, wait_time=5, delay_time=0.1):
    driver = webdriver.Chrome('chromedriver')

    driver.implicitly_wait(wait_time)

    driver.get(url)

    while True:

        try:
            more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            more.click()
            time.sleep(delay_time)

        except:
            break

    nicknames = driver.find_elements_by_css_selector('span.u_cbox_nick')
    list_nicknames = [nick.text for nick in nicknames]


    datetimes = driver.find_elements_by_css_selector('span.u_cbox_date')
    list_datetimes = [datetime.text for datetime in datetimes]

  
    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    list_contents = [content.text for content in contents]

    likes = driver.find_elements_by_css_selector('em.u_cbox_cnt_recomm')
    list_likes=list()
    for like in likes:
        list_likes.append(like.text)


    disLikes=driver.find_elements_by_css_selector('em.u_cbox_cnt_unrecomm')
    list_disLikes=list()
    for disLike in disLikes:
        list_disLikes.append(disLike.text)


    list_sum = list(zip(list_nicknames, list_datetimes, list_contents,list_likes,list_disLikes))

    driver.quit()

    return list_sum


if __name__ == '__main__':


    url = 'https://n.news.naver.com/mnews/article/comment/025/0003189664?sid=101'

    comment_data=get_naver_news_comments(url)


    comments = get_naver_news_comments(url)


    col = ['작성자', '날짜', '내용','좋아요','싫어요']


    df = pd.DataFrame(comments, columns=col)

    df.to_excel('news.xlsx', sheet_name='뉴스 기사 제목')
