import os
from slugify import slugify

class Article:
    def __init__(self, title):
        self.title = title
        self.content = ""

    @property
    def slug(self):
        return slugify(self.title)

    def load_content(self):
        with open(f"articles/{self.title}") as file:
            self.content = file.read()

    @classmethod
    def all(cls):
        titles = os.listdir("articles")
        articles = {}
        for title in titles:
            article = cls(title)
            article.load_content()
            articles[article.slug] = article

        return articles