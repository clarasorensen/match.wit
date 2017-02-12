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
    return password == hashlib.sha256(salt.encode()+userpw.encode()).hexdigest(