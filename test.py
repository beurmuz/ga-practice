# 크롤링시 필요한 라이브러리 import
from bs4 import BeautifulSoup
import requests
import csv
import json

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

# json 형식으로 만들기
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
  json.dump(newsData, f_write, ensure_ascii=False, indent=4)

# 생성된 data.js 파일을 읽어서 파일에 변수명 추가하기
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
  line = f.readline()
  while line:
    data += line
    line = f.readline()

final_data = f"let newsData = {data}"
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
  f_write.write(final_data)
