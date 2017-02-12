#!/usr/local/bin/python2.7

import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = '\xa7L"\x17>\x9bR:\x92"H\xb6\\k]\x00\xdc4\x85\xa6\xa2\xdd\xa5\x83'

@app.route('/', methods=['GET', 'POST'])
def home():
    # render the home page
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()