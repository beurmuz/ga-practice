import requests
from bs4 import BeautifulSoup

url = 'https://ridibooks.com/category/new-releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

#__next > main > div > section > ul.fig-1rl9mz1 > li:nth-child(1) > div > div.fig-smbj6f > div > div:nth-child(1) > a
bookservices = soup.select('.fig-rs5q24')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
