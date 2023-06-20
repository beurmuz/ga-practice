# 크롤링시 필요한 라이브러리 import
from bs4 import BeautifulSoup
import requests

# ConnectionError 방지용
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Whale/3.21.192.18"}


url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=식케이&start=1"
news = requests.get(url, headers=headers)
newsHtml = BeautifulSoup(news.text,"html.parser")
totalNews = newsHtml.select('div.news_area')

newsData = []

for i in range(len(totalNews)):
  m = totalNews[i]
  newsData.append({
      "id": i,
      "title": m.select_one('a.news_tit')['href'],
      "date": m.select_one('span.info').text,
      "content": m.select_one('div.dsc_wrap > a.api_txt_lines.dsc_txt_wrap').text,
      "date": m.select_one('span.info').text,
      "media": m.select_one('a.info.press').text
  })
  # totalURL.append(m.select_one('a.news_tit')['href'])

print(newsData)
