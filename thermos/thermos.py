from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

def store_bookmark(url):
    bookmarks.append({
        'url': url,
        'user': 'tiziano',
        'date': datetime.now()
    })

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('Stored url: {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html', pagename='add')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
