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
    account = form['account']
    for k,v in form.items():
        print k
        print v
    curs.execute('INSERT INTO accounts VALUES (%s,%s,%s);', (form['email'],hash_password(form['password']),account))
    if account=="mentor":
    	curs.execute('INSERT INTO mentor_survey (email, name, communication, age, location, gender, spokenLang, relationshipGoals, mentorType, occupationMentor, codingLang, resume, mentorBio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', (form['email'],form['name'],form['communication'],form['age'],form['location'],form['gender'],form['spokenLang'],form['relationshipGoals'],form['mentorType'],form['occupationMentor'],form['codingLang'],form['resume'],form['mentorBio']))
    if account == "mentee":
        curs.execute('INSERT INTO mentee_survey VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', (form['email'],form['name'],form['communication'],form['age'],form['location'],form['gender'],form['spokenLang'],form['relationshipGoals'],form['mentorType'],form['occupationMentee'],form['interests']))

def empassCheck(email,pw):
    '''checks to make sure the given email and password matches the ones \
in the user database table'''
    curs = connect()
    # first checks if email exists in database                            
    curs.execute('SELECT password FROM accounts WHERE email=%s;',(email,)\
)
    row = curs.fetchone()
    if row is None:
	return 0 # when email does not exist in database                  
    else:
       if check_password(row['password'],pw):
           return 1 # username and password matched                          
       else:
           return 0 # username and password does not match 
	
def searchEmail(email):
    '''searches if the email is already in db'''
    curs = connect()
    curs.execute('SELECT * FROM accounts WHERE email=%s;',(email,))
    row = curs.fetchone()
    if row:
    	return 1
    else: 
    	return 0

def showMentor(mentee_email):
	''' finds the mentor '''
	curs = connect()
	# mentor = curs.execute('SELECT mentor_survey.email FROM `match` WHERE `match`.mentee_email=%s;', (mentee_email,))
	curs.execute('SELECT mentor_survey.name, mentor_survey.email FROM mentor_survey, `match` WHERE `match`.mentee_email=%s AND mentor_survey.email=`match`.mentor_email;',(mentee_email,))
	return curs.fetchall()

def showMentee(mentor_email):
	''' finds the mentees '''
	curs = connect()
	curs.execute('SELECT mentee_survey.name, mentee_survey.email FROM mentee_survey, `match` WHERE `match`.mentor_email=%s AND mentee_survey.email=`match`.mentee_email ORDER BY mentee_survey.name;', (mentor_email,))
	return curs.fetchall()

def accountType(email):
    ''' returns the account type '''
    curs = connect()
    curs.execute('SELECT type FROM accounts WHERE email = %s;', (email,))
    return curs.fetchone()

def addMatch(mentee, mentor):
    ''' adds match emails to match table '''
    curs = connect()
    curs.execute('INSERT INTO `match` VALUES (%s,%s);', (mentee, mentor))

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



