#!/usr/bin/python
import dbmobile_model

from config import database
from sqlalchemy import orm
from sqlalchemy import create_engine

connection_string ="mysql://%s:%s@%s/%s" % (
	database['user'], 
	database['pass'],
	database['server'],
	database['name'])

# Create an engine an create all the tables we need
engine = create_engine(connection_string, echo=True)

dbmobile_model.metadata.bind = engine
dbmobile_model.metadata.create_all()

# Set up the session
sm = orm.sessionmaker(
	bind=engine, 
	autoflush=True, 
	autocommit=False,
	expire_on_commit=True)

# Options:
#		bind = engine 		-> this binds the session to the engine, the session will automatically create the connections it needs
#		autoflush = True 	-> if you commit your changes to the database before they have been flushed, this option tells SQLAlchemy to flush them before the commit is gone.
# 	autocommit = False-> this tells SQLAlchemy to wrap all changes between commits in a transaction	
#		expire_on_commit = True -> this means that all instances attached to the session will be fully expired after each commit so that all attribute/object access subsequent to a completed transaction will load from the most recent database state
session = orm.scoped_session(sm)
