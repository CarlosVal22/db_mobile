#!/usr/bin/python

from sqlalchemy import orm
import datetime
from sqlalchemy import schema, types

metadata = schema.MetaData()

def now():
	return datetime.datetime.now()

users_table = schema.Table('Users', metadata,
	schema.Column('id', types.Integer, 
		schema.Sequence('user_id', optional=True), primary_key=True),
	schema.Column('password', 		types.Unicode(20),	nullable=False),
	schema.Column('age', 					types.Integer,	 		default=u''),
	schema.Column('gender', 			types.Unicode(20), 	default=u''),
	schema.Column('postal_code', 	types.Unicode(20), 	default=u''),
	schema.Column('browser', 			types.Unicode(100), default=u''),
	schema.Column('source_ip', 		types.Unicode(15), 	default=u''),
	schema.Column('created', 			types.TIMESTAMP(), 	default=now()),
)

questionaire_table = schema.Table('Questionaire', metadata,
	schema.Column('id', types.Integer, 
		schema.Sequence('questionaire_id', optional=True), primary_key=True),
	schema.Column('userid', 			types.Integer,
		schema.ForeignKey('Users.id'), nullable=False),
	schema.Column('step1', 				types.Float, 				default=0),
	schema.Column('step2', 				types.Float, 				default=0),
	schema.Column('step3', 				types.Float, 				default=0),
	schema.Column('step4', 				types.Float, 				default=0),
	schema.Column('step5', 				types.Float, 				default=0),
	schema.Column('step6', 				types.Float, 				default=0),
	schema.Column('step7', 				types.Float, 				default=0),
	schema.Column('scale7shq', 		types.Float,				default=0),
	schema.Column('diener', 			types.Float,				default=0),
	schema.Column('love', 				types.Integer,			default=0),
	schema.Column('health', 			types.Integer,			default=0),
	schema.Column('job', 					types.Integer,			default=0),
	schema.Column('browser', 			types.Unicode(100),	default=u''),
	schema.Column('source_ip', 		types.Unicode(15),	default=u''),
	schema.Column('created', 			types.TIMESTAMP(), 	default=now()),
)

reminder_table = schema.Table('Reminder', metadata,
	schema.Column('id', 					types.Integer, 
		schema.Sequence('reminder_id', optional=True), primary_key=True),
	schema.Column('userid', 			types.Integer,
		schema.ForeignKey('Users.id'), nullable=False),
	schema.Column('grade', 				types.Integer,			default=0),
	schema.Column('created', 			types.TIMESTAMP(), 	default=now()),
)
# Options:
#  primary_key
#  foreign_key
#  sequence
#  unique=True -> To enforce UNIQUE constraints

# Create a class per table without data
class Users(object):
	pass

class Questionaire(object):
	pass

class Reminder(object):
	pass

# Map the class with its table
#orm.mapper(Users, users_table, properties={
#    'questionaire':orm.relation(Questionaire, backref='Users')
#})

orm.mapper(Users, users_table)
orm.mapper(Questionaire, questionaire_table)
orm.mapper(Reminder, reminder_table)
