from bs4 import BeautifulSoup
import requests

url = "https://namu.wiki/w/%EC%B2%AD%EB%8B%B4%EC%96%B4%ED%95%99%EC%9B%90"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.select_one("div > div.mh744BrF > div:nth-child(8) > div \
> div > div:nth-child(2) > div > div > div > div > div > div > div > div:nth-child(13) > div:nth-child(1)\
 > div > div:nth-child(8) > div").text

print(posts)
