import os

from flask import Flask, render_template
from slugify import slugify

app = Flask(__name__)


def read_articles():
    articles = os.listdir('articles')
    article_dict = {}
    for article in articles:
        article_dict.update({slugify(article): article})
    return article_dict


@app.route('/')
def blog():
    return render_template('blog.html', articles=read_articles())

@app.route('/blog/<slug>')
def article(slug: str):
    articles = read_articles()
    article = articles[slug]
    with open('articles/' + article, 'r') as article_content:
        content = article_content.read()
    return render_template('article.html', content=content, title=article)


if __name__ == '__main__':
    app.run(debug=True)