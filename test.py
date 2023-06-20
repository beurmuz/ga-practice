import requests
from bs4 import BeautifulSoup

url = 'https://vibe.naver.com/artist/331653/tracks?artistTrackType=RELEASE'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('.song')
for no, title in enumerate(songs, 1):
    print(no, title.text.strip())
