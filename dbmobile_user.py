#!/usr/bin/env python

import cgitb; cgitb.enable()

import myrandompassword

import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import Users

def init(ip=None,browser=None):
	user = dbmobile_model.Users()
	user.password = usr_passwd = myrandompassword.generator()
	user.browser = browser
	user.source_ip = ip
	session.add(user)
	session.commit()
	return user

def add( age, gender, postal_code):
	user = dbmobile_model.Users()
	user.age = age
	user.gender = gender
	user.postal_code = postal_code
	user.browser = mybrowserdata.agent
	user.source_ip = mybroserdata.ip
	session.add(user)
	session.commit()

def first():
	item = session.query(Users).first()

def last():
	item = session.query(Users).last()

def remove(value):
	item = session.query(Users).filter_by(id=value).delete()

def get(value):
	item = session.query(Users).filter_by(id=value).first()
	if item is None:
		return None
	return item

def modify(value):
	session.add(value)
	session.commit()

def update():
	pass

def getall():
	users_q = session.query(Users)
	for item in users_q:
		 print "%s\t%s\t%s" % (item.id,item.password,item.created)

def checkuser(userid,passwd):
	user = get(userid)
	if user is None:
		return None

	if passwd != user.password:
		return None

	return user
