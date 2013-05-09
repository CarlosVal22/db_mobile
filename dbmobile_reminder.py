#!/usr/bin/env python

import cgitb; cgitb.enable()

import dbmobile_model
from dbmobile_conn import session
from dbmobile_model import Users,Questionaire

def init():
	item = dbmobile_model.Reminder()
	return item

def add(item):
	session.add(item)
	session.commit()
	return item
