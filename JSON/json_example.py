import json
from requests import get
from requests.exceptions import RequestException


class Post:
    def __init__(self, userId: int, id: int, title: str, body: str):
        self.user_id = userId  # Mapping 'userId' to 'user_id'
        self.post_id = id  # Mapping 'id' to 'post_id'
        self.title = title
        self.body = body

    def __str__(self):
        return f"Post ID: {self.post_id}\nUser ID: {self.user_id}\nTitle: {self.title}\nBody: {self.body}\n"


url = 'https://jsonplaceholder.typicode.com/posts'

try:
    response = get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Assuming the response contains JSON data
    posts_data = response.json()

    # converting to list of post
    posts_list = [Post(**post_data) for post_data in posts_data]

    print(type(posts_list))

    for post in posts_list:
        print(str(post))

    json_string = json.dumps(posts_data, indent=4)
    print(json_string)

    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts_data, f, ensure_ascii=False, indent=4)

except RequestException as e:
    print(f"Error fetching data: {e}")
