import requests
from datetime import datetime
import ssl

print(ssl.OPENSSL_VERSION)

url = "https://www.reddit.com/r/apple/new.json"
headers = {"User-Agent": "MyAPI/0.0.1"}

response = requests.get(url, headers=headers)
data = response.json()

post_count = 1
for post in data["data"]["children"]:
    title = post["data"]["title"]
    body_text = post["data"]["selftext"]
    author = post["data"]["author"]

    up_vote = post["data"]["ups"]
    down_vote = post["data"]["downs"]
    vote_ratio = post["data"]["upvote_ratio"]
    num_comments = post["data"]["num_comments"]
    url_link = post["data"]["url"]
    time = post["data"]["created_utc"]
    time = datetime.utcfromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S UTC")

    print(f"\n========== Post {post_count} ==========")
    print(f"Title: {title}")
    if body_text:
        print(f"Description: {body_text[0:180]}")
    print(f"By: {author}\n")
    print(f"Vote stats: Up ({up_vote}), Down ({down_vote}), Ratio ({vote_ratio})")
    print(f"Number of comments: {num_comments}")
    if url_link:
        print(f"Attached URL: {url_link}")
    print(f"timestamp: {time}")

    post_count += 1
