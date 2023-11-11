from bs4 import BeautifulSoup
import requests

url = "https://namu.wiki/w/%EB%98%A5"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.select_one("div > div.mh744BrF > div:nth-child(8) > div > div > div:nth-child(2) > div > div > div > div > div > div > div > div:nth-child(13) > div:nth-child(1) > div > div:nth-child(11) > div").text

print(posts)