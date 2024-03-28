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

    def get_post_info(self) -> str:
        return (f"User: {self.author.username}\n"
                f"Email: {User.convert_email_to_lowercase(self.author.email)}\n"
                f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Likes: {self.likes_qty}")


class Forum:
    total_comments = 0

    def __init__(self) -> None:
        self.posts = []

    def add_post(self, single_post: Post) -> None:
        self.posts.append(single_post)
        Forum.total_comments += 1

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
