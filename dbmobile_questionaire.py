#!/usr/bin/env python

import cgitb; cgitb.enable()

import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import Users,Questionaire

def init():
	item = dbmobile_model.Questionaire()
	item.created = "from_unixtimestamp()"
	return item

def add(item):
	session.add(item)
	session.commit()
	return item

#def first():
#	item = session.query(Users).first()

#def last():
#	item = session.query(Users).last()

#def remove(value):
#	item = session.query(Users).filter_by(id=value).delete()

#def get(value):
#	item = session.query(Users).filter_by(id=value).first()
#	if item is None:
#		return None
#	return item

#def modify(value):
#	session.add(value)
#	session.commit()

#def update():
#	pass

#def getall():
#	users_q = session.query(Users)
#	for item in users_q:

