from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import uri 
from flaskext.markdown import Markdown

from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

app = Flask(__name__)
Markdown(app)
#login_manager = LoginManager()

app.config['SQLALCHEMY_DATABASE_URI'] = uri.uri()

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

"""
@app.route("/add")
def add():
    return render_template("add.html")
"""

@app.route('/add', methods=['POST', 'GET'])
def addpost():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        if request.form['']
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']

        post = blogs(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

"""# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)"""



if __name__ == '__main__':
 app.run(debug=True)

