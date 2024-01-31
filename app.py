import hashlib

from slugify import slugify
from flask import Flask, render_template, request, session, redirect
from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"

articles = Article.all()

users = {
    "admin": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}


@app.route('/')
def blog():
    articles = Article.all()
    return render_template('blog.html', articles=articles)


@app.get('/admin')
def admin_page():
    if "user" in session:
        return "You are already authenticated"
    return render_template('login.html')


@app.post('/admin')
def admin_login():
    username = request.form['username']
    password = request.form['password']

    if username not in users:
        return render_template("login.html", error="username/password is incorrect")

    hashed = hashlib.sha256(password.encode('ascii')).hexdigest()
    if hashed != users[username]:
        return render_template("login.html", error="username/password is incorrect")

    session['user'] = username

    return redirect('/new-post')


@app.get('/logout')
def logout():
    try:
        del session["user"]
    except KeyError:
        return "You are already logged out"
    return "You are now logged out"


@app.route("/blog/<slug>")
def article(slug: str):
    try:
        return render_template("article.html", article=articles[slug])
    except KeyError:
        return "Not found", 404

@app.get('/new-post')
def new_post_page():
    if not is_authenticated():
        return redirect('/admin')
    return render_template('new_post.html')


@app.post('/new-post')
def create_new_post():
    if not is_authenticated():
        return redirect('/admin')
    title = request.form['title']
    body = request.form['body']
    if articles.get(slugify(title), None):
        return render_template('new_post.html', error="Article already exists")

    Article.create(title=title, content=body)
    return redirect('/')


def is_authenticated():
    if "user" in session:
        return True
    return False


if __name__ == '__main__':
    app.run(debug=True)
