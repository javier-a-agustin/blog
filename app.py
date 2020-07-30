from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import sys
import uri 
from flaskext.markdown import Markdown

from datetime import datetime
import locale

#locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

app = Flask(__name__)

Markdown(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = uri.uri()

db = SQLAlchemy(app)

class blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

class users(db.Model):
    name = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200))

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

@app.route('/add', methods=['POST', 'GET'])
def addpost():
    if request.method == 'GET':
        if session.get('name') is None:
            return redirect(url_for('login'))
        else:
            return render_template("add.html")
    else:
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = "Javier Fernandez"
        content = request.form['content']

        post = blogs(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        if session.get('name') is None:
            return render_template("login.html")
        else:
            return redirect(url_for('addpost'))
    else:
        name = request.form['name']
        password = request.form['password']
        
        user = users.query.filter_by(name=name, password=password).all()
        if user == []:
            return redirect(url_for('login')) 
        else:
            session['name'] = name
            return redirect(url_for('addpost'))

@app.route("/logout")
def logout():
    session['name'] = None
    return redirect(url_for('index'))

if __name__ == '__main__':
 app.run()

