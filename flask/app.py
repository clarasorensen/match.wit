#!/usr/local/bin/python2.7

import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = '\xa7L"\x17>\x9bR:\x92"H\xb6\\k]\x00\xdc4\x85\xa6\xa2\xdd\xa5\x83'

@app.route('/', methods=['GET', 'POST'])
def home():
    # render the home page
    return render_template('index.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
	return render_template('signup.html')

@app.route('/1/', methods=['GET', 'POST'])
def one():
	return render_template('1.html')

@app.route('/2/', methods=['GET', 'POST'])
def two():
	return render_template('2.html')

@app.route('/3/', methods=['GET', 'POST'])
def three():
	return render_template('3.html')

@app.route('/4/', methods=['GET', 'POST'])
def four():
	return render_template('4.html')

@app.route('/5/', methods=['GET', 'POST'])
def five():
	return render_template('5.html')

@app.route('/6/', methods=['GET', 'POST'])
def six():
	return render_template('6.html')

@app.route('/7/', methods=['GET', 'POST'])
def seven():
	return render_template('7.html')

@app.route('/8/', methods=['GET', 'POST'])
def eight():
	return render_template('8.html')

@app.route('/9/', methods=['GET', 'POST'])
def nine():
	return render_template('9.html')

@app.route('/10/', methods=['GET', 'POST'])
def ten():
	return render_template('10.html')

@app.route('/11/', methods=['GET', 'POST'])
def eleven():
	return render_template('11.html')

@app.route('/12/', methods=['GET', 'POST'])
def twelve():
	return render_template('12.html')

@app.route('/13/', methods=['GET', 'POST'])
def thirteen():
	return render_template('13.html')

@app.route('/emailpass/', methods=['GET', 'POST'])
def emailpass():
	return render_template('emailpass.html')

@app.route('/location/', methods=['GET', 'POST'])
def location():
	return render_template('location.html')

@app.route('/language/', methods=['GET', 'POST'])
def language():
	return render_template('language.html')

if __name__ == '__main__':
    app.debug = True
    app.run()