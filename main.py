import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

main_section = soup.find("div", {"class": "group_type is_activate"})
top_news_ul = main_section.find("tbody")

top_news = top_news_ul.find_all("th")

for article in top_news:
    print(article.get_text())
