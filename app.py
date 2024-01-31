import hashlib

from flask import Flask, render_template, request, session
from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"


articles = Article.all()

users = {
    "admin": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}


@app.route('/')
def blog():
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

    return "you are now authenticated"


@app.route("/blog/<slug>")
def article(slug: str):
    return render_template("article.html", article=articles[slug])


if __name__ == '__main__':
    app.run(debug=True)
