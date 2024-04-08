from typing import List


class User:
    users_qty = 0

    def __init__(self, username: str, email: str):
        self.email = email
        self.username = username
        User.users_qty += 1

    def info(self):
        print(f"User {self.username} has email {self.email}")

    @staticmethod
    def get_total_users():
        return User.users_qty

    @staticmethod
    def convert_email_to_lowercase(original_email: str) -> str:
        return original_email.lower()


first_user = User(username="damiansoch", email="dSa@dS.pl")
second_user = User(username="kingasoch", email="ks@ks.Com")


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.author = author
        self.content = content
        self.title = title
        self.likes_qty = 0

    def like(self) -> None:
        self.likes_qty += 1

    # defining magic method in your own class
    def __add__(self, other):
        return (f"{self.content} {other.content}", self.likes_qty + other.likes_qty)

    def __eq__(self, other):
        return self.title == other.title

    def get_post_info(self) -> str:
        return (f"User: {self.author.username}\n"
                f"Email: {User.convert_email_to_lowercase(self.author.email)}\n"
                f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Likes: {self.likes_qty}")


class Forum:
    total_comments = 0

    def __init__(self) -> None:
        self.users: List[User] = []
        self.posts: List[Post] = []

    def add_post(self, single_post: Post) -> None:
        self.posts.append(single_post)
        if not self.username_present(single_post.author.username, self.users):
            self.users.append(single_post.author)
        Forum.total_comments += 1

    @staticmethod
    def username_present(username: str, users: list[User]):
        is_present = False
        for single_user in users:
            if single_user.username == username:
                is_present = True
        return is_present

    def print_posts(self) -> None:
        for post in self.posts:
            print(post.get_post_info())
            print("-----------------------------")

        print(f"Total comments: {self.total_comments}")
        print(f"Total users: {User.get_total_users()}")

    def like_selected_post(self, post_index: int):
        if 0 <= post_index < len(self.posts):
            self.posts[post_index].like()
        else:
            print("Post index out of range")

    def find_user_by_username(self, username):
        return next((user for user in self.users if user.username == username), None)

    def find_all_post_by_username(self, username: str):
        if self.find_user_by_username(username):
            return [post for post in self.posts if post.author.username == username]
        else:
            return None


forum = Forum()

post1 = Post(title="First Post", content="This is a first post content", author=first_user)
post2 = Post(title="Second Post", content="This is a second post content", author=second_user)
post3 = Post(title="Third Post", content="This is a third post content", author=second_user)

forum.add_post(post1)
forum.add_post(post2)
forum.add_post(post3)

forum.like_selected_post(0)
forum.like_selected_post(0)
forum.like_selected_post(0)
forum.like_selected_post(1)
forum.like_selected_post(1)

forum.print_posts()

print()
print("allUsers info")
for author in forum.users:
    author.info()

print()

# using user defined method in the custom-made class
print(forum.posts[0] + forum.posts[1])
print(forum.posts[0] == forum.posts[0])

print()

print("user lookup")

username_to_find = "kingasoch"
found_user = (forum.find_user_by_username(username_to_find))
if found_user:
    print(found_user.__dict__)
else:
    print(f"No user found with username: {username_to_find}")

print()
print("posts by username lookup")

found_posts = forum.find_all_post_by_username(username_to_find)
if found_posts:
    for s_post in found_posts:
        print(s_post.get_post_info())
else:
    print(f"No posts for user: \"{username_to_find}\" found")
