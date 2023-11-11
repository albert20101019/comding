from bs4 import BeautifulSoup
import requests

url = "https://namu.wiki/w/%EC%BD%94%EB%94%A9"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.select_one("div > div.mh744BrF > div:nth-child(8) > div > div > div:nth-child(2) > div > div > div > div > div > div > div > div:nth-child(13) > div:nth-child(1) > div > div:nth-child(5) > div:nth-child(1)").text

print(posts)