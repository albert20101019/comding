from bs4 import BeautifulSoup
import requests

url = "https://orbi.kr/list/tag/%EC%9E%85%EC%8B%9C%EC%9E%90%EB%A3%8C,%EC%B6%94%EC%B2%9C"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.select(".list-text")

def extract_post_data(post):
    try:
        title = post.select_one(" div.list-text > p.title > a").text.strip()
    except:
        title = "내용없음"
    try:
        content = post.select_one("div.list-text > p.content").text
    except:
        content = "내용 없음"
    try:
        comment = post.select_one("span.comment-count").text
    except:
        comment = "내용없음"
    return title, content, comment

for post in posts:
    title, content,comment = extract_post_data(post)
    if "정시" in title:
        print("[중요] 정시대비정보")
    elif "수시" in title:
        print("수시대비정보")
    print("제목:", title)
    print("내용:", content)
    print("댓글수:", comment)
    print("-----------")