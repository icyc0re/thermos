from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = b'\x856\xe6L\nt\xe6\xb5\xa1\x7f\xc0gA\xf1\xd2\xeb%\xd2FPs\xa1\xe3A'

bookmarks = []

def store_bookmark(url):
    bookmarks.append({
        'url': url,
        'user': 'tiziano',
        'date': datetime.now()
    })

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda x: x['date'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', last_bookmarks=new_bookmarks(5))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        flash('Stored bookmark: {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html', pagename='add')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
