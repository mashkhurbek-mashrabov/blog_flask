from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blog():
    return render_template('blog.html')

@app.route('/blog/<slug>')
def article(slug: str):
    return render_template('article.html')



if __name__ == '__main__':
    app.run(debug=True)