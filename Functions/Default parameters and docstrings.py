from datetime import date


def get_weekday() -> str:
    """Returns current day of the week"""
    return date.today().strftime("%A")


def create_new_post(post, weekday=get_weekday()):
    """
    Returns post with created_on -> weekday
    :param dict post: Post to be manipulated
    :param str weekday: Optional -> day of the week
    :return: New post with created_on -> weekday
    """
    post_copy = post.copy()
    post_copy["created_on"] = weekday
    return post_copy


initial_post = {
    "id": 2456,
    "author": "Damian"
}

post_with_weekday = create_new_post(post=initial_post)
print(post_with_weekday)
