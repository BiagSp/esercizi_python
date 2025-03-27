"""
Metodi di lettura degli url 

"""

import requests


url = "https://jsonplaceholder.typicode.com/posts"

posts = requests.get(url).json()

"""for post in posts[0].keys():
    print(post)


#stampiamo tutte le chiavi uniche in tutti gli elementi 

all_keys = set()

for post in posts:
    for key in post.keys():
        all_keys.add(key)

for key in all_keys:
    print(key)
"""
user_id = []

for post in posts:
    if post["userId"]:
        user_id.append(post["userId"])
    else:
        print(f"No userId in {post["id"]}")
    print(post.keys())



for item in posts:
    if isinstance(item, dict) and "body" in item:
        print(f"Capitalize: \n {item['body'].upper()}")
