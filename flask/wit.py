#!/usr/local/bin/python2.7

# Functions for flask app

import uuid # for hashing password
import random # for hashing password
import hashlib # for hashing password
import MySQLdb
import dbconn2

def connect():
	'''Connects to the MySQL db using the dsn.cnf file and returns a cursor'''
	dsn = dbconn2.read_cnf('dsn.cnf')
	dsn['db'] = 'whack17'
	conn = dbconn2.connect(dsn)
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	return curs

def createAccount(form):
	''' creates an account in the db with the survey results based on the form '''
	curs = connect()
	type = form['type']
	row = searchEmail(form['email'])
	if row == None:
		curs.execute('INSERT INTO accounts VALUES (%s,%s,%s);', (form['email'],hash_password(form['password']),type))
		if type=="mentor":
			curs.execute('INSERT INTO mentor_survey VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', (form['email'],form['name'],form['communication'],form['age'],form['location'],form['gender'],form['spokenLang'],form['relationshipGoals'],form['mentorType'],form['occupationMentor'],form['codingLang'],form['resume'],form['resume'],form['mentorBio']))
		if type == "mentee":
			curs.execute('INSERT INTO mentee_survey VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', (form['email'],form['name'],form['communication'],form['age'],form['location'],form['gender'],form['spokenLang'],form['relationshipGoals'],form['mentorType'],form['occupationMentee'],form['interests']))
		return 1
	else:
		return 0


	
def searchEmail(email):
    '''searches if the email is already in db'''
    curs = connect()
    curs.execute('SELECT * FROM accounts WHERE email=%s;',(email,))
    row = curs.fetchall()
    return row

def hash_password(password):
    '''returns the hashed password with a random salt'''
    #uuid is used to generate a random number
    salt = (uuid.uuid4().hex)[:5]
    # hashedpw is the hashed password with the salt concatenated at the end
    hashedpw = hashlib.sha256(salt.encode()+password.encode()).hexdigest() + ':' + salt
    return hashedpw
   
def check_password(hashedpw,userpw):
    '''checks if the user input password is the same as the hashed password'''
    password, salt = hashedpw.split(':')
    return password == hashlib.sha256(salt.encode()+userpw.encode()).hexdigest()



