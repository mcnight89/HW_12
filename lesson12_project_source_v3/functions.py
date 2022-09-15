import json


def load_posts():
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def search_by_word(word):
    """Тянем несколько постов"""
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post
