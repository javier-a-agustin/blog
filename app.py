from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from flasktext.markdown import Markdown

from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

app = Flask(__name__)
#Markdown(app)

# new db postgres://udharpzdqpmawc:2ff2b461f8114b3dd92347f937c680520ccbd2fe56de5f3fdf6028586c41fe15@ec2-54-236-169-55.compute-1.amazonaws.com:5432/d8971805l1evh0
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://udharpzdqpmawc:2ff2b461f8114b3dd92347f937c680520ccbd2fe56de5f3fdf6028586c41fe15@ec2-54-236-169-55.compute-1.amazonaws.com:5432/d8971805l1evh0"

db = SQLAlchemy(app)


class blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route("/")
def index():
    posts = blogs.query.all()

    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def post(post_id):
    post = blogs.query.filter_by(id=post_id).one()

    return render_template("post.html", post=post)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = blogs(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/meter", methods=['POST', 'GET'])
def meter():
    return render_template("meter.html")

if __name__ == '__main__':
 app.run(debug=True)

