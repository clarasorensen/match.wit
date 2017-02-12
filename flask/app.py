#!/usr/local/bin/python2.7

import os
from wit import *
from flask import Flask, render_template, request, redirect, url_for, flash,\
 session

app = Flask(__name__)
app.secret_key = '\xa7L"\x17>\x9bR:\x92"H\xb6\\k]\x00\xdc4\x85\xa6\xa2\xdd\xa5\x83'

user = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    # render the home page
    return render_template('index.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        ty = request.form['account']
        user['account'] = ty
        return redirect(url_for('one'))
    else:
        return render_template('signup.html')

@app.route('/1/', methods=['GET', 'POST'])
def one():
    if request.method == 'POST':
        email = request.form['email']
        exist = searchEmail(email)
        password = request.form['password']
        user['email'] = email
        user['password'] = password
        if exist:
            flash('account with the email already exists')
            return redirect(url_for('one'))
            
        else:
            return redirect(url_for('two'))
    else:
        return render_template('1.html')

@app.route('/2/', methods=['GET', 'POST'])
def two():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        user['name'] = name
        user['age'] = age
        user['gender'] = gender
        return redirect(url_for('three'))
    else:
        return render_template('2.html')

@app.route('/3/', methods=['GET', 'POST'])
def three():
    if request.method == 'POST':
        location = request.form['location']
        user['location'] = location
        return redirect(url_for('four'))
    else:
	   return render_template('3.html')

@app.route('/4/', methods=['GET', 'POST'])
def four():
    if request.method == 'POST':
        spokenLang = request.form.getlist('spokenLang') 
        string = ""
        for s in spokenLang:
        	string += s
        user['spokenLang'] = string
        return redirect(url_for('five'))
    else:
	   return render_template('4.html')

@app.route('/5/', methods=['GET', 'POST'])
def five():
    if request.method == 'POST':
        communication = request.form.getlist('communication') 
        string = ""
        for s in communication:
        	string += s
        user['communication'] = string
        return redirect(url_for('six'))
    else:
	   return render_template('5.html')

@app.route('/6/', methods=['GET', 'POST'])
def six():
    if request.method == 'POST':
        relationshipGoals = request.form['relationshipGoals']
        user['relationshipGoals'] = relationshipGoals
        return redirect(url_for('seven'))
    else:
	   return render_template('6.html')

@app.route('/7/', methods=['GET', 'POST'])
def seven():
    if request.method == 'POST':
        mentorType = request.form.getlist('mentorType') 
        string = ""
        for s in mentorType:
        	string += s
        user['mentorType'] = string
        return redirect(url_for('eight'))
    else:
	   return render_template('7.html')

@app.route('/8/', methods=['GET', 'POST'])
def eight():
    if request.method == 'POST':
        occupationMentor = request.form['occupationMentor']
        user['occupationMentor'] = occupationMentor
        if user['account'] == "mentee":
            return redirect(url_for('twelve'))
        else:
            return redirect(url_for('nine'))
    else:
	   return render_template('8.html')

@app.route('/9/', methods=['GET', 'POST'])
def nine():
    if request.method == 'POST':
        codingLang = request.form.getlist('codingLang')
        string = ""
        for s in codingLang:
        	string += s
        user['codingLang'] = string
        return redirect(url_for('ten'))	
    else:
        return render_template('9.html')

@app.route('/10/', methods=['GET', 'POST'])
def ten():
    if request.method == 'POST':
        resume = request.form['resume']
        user['resume'] = resume
        return redirect(url_for('eleven'))	
    else:
	   return render_template('10.html')

@app.route('/11/', methods=['GET', 'POST'])
def eleven():
    if request.method == 'POST':
        mentorBio = request.form['mentorBio']
        user['mentorBio'] = mentorBio
        createAccount(user)
        # user = {}
        flash('account has been successfully added')
        flash('') # return results
        return redirect(url_for('resources'))
    else:	
	   return render_template('11.html')

@app.route('/12/', methods=['GET', 'POST'])
def twelve():
    if request.method == 'POST':
        occupationMentee = request.form['occupationMentee']
        user['occupationMentee'] = occupationMentee
        return redirect(url_for('thirteen'))
    else:
	   return render_template('12.html')

@app.route('/13/', methods=['GET', 'POST'])
def thirteen():
    if request.method == 'POST':
        interests = request.form['interests']
        user['interests'] = interests
        createAccount(user)
        session['email'] = user['email']
        session['logged_in'] = True
       	flash('account has been successfully added')
        # result = 
        # addMatch(session['email'], result['email'])
        flash('') # return results
        return redirect(url_for('resources'))
    else:
	   return render_template('13.html')

@app.route('/login/', methods=['GET','POST'])
def logIn():
    if 'email' in session:
        if request.method == 'GET':
            session.pop('email', None)
            session['logged_in'] = False
            flash('You are now logged out.')
            return redirect(url_for('logIn'))
    else:
        if request.method == 'POST':
            loginemail = request.form['loginemail']
            loginpassword = request.form['loginpassword']
            log = empassCheck(loginemail,loginpassword)
            if log == 0:
                flash('invalid email/password')
                return redirect(url_for('logIn'))
            if log == 1:
                flash('successfully logged in as ' + loginemail)
                session['logged_in'] = True
                session['email'] = loginemail
                return redirect(url_for('resources'))
    return render_template('login.html')

@app.route('/resources/', methods=['GET','POST'])
def resources():
    if 'email' in session:
        if accountType(session['email']) == "mentor":
            mentee = showMentee(session['email'])
            flash('Your mentee(s) are ')
            flash(mentee)
        else:
            mentor = showMentor(session['email'])
            flash('Your mentor is ')
            flash(mentor)
    return render_template('resources.html')

if __name__ == '__main__':
    app.debug = True
    app.run()