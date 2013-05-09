from mod_python import apache
from mod_python import util

import dbmobile_user 
import dbmobile_questionaire 
import dbmobile_reminder
import dbmobile_log

from dbmobile_log import ErrorLevel

OK=0
NOK=1

def LogFunction(name=None,user=None,passwd=None,**params):
	dbmobile_log.writeInLog(name, ErrorLevel.Log)
	dbmobile_log.writeInLog(" user  :*%s*" % user, ErrorLevel.Log)
	dbmobile_log.writeInLog(" passwd:*%s*" % passwd, ErrorLevel.Log)
	dbmobile_log.writeInLog(" params:%s" % params, ErrorLevel.Log)

def index(req):
	req.content_type = "text/plain"
	req.send_http_header()

	dbmobile_log.IP = req.subprocess_env.get("REMOTE_ADDR")
	dbmobile_log.writeInLog("Index", ErrorLevel.Log)
	return apache.OK

def createuser(req):
  req.add_common_vars()
  newuser = dbmobile_user.init(
    req.subprocess_env.get("REMOTE_ADDR"),
    req.subprocess_env.get("HTTP_USER_AGENT")
    )

  dbmobile_log.IP = req.subprocess_env.get("REMOTE_ADDR")

  if newuser is None:
    dbmobile_log.writeInLog("CreateUser", ErrorLevel.Err)
    return 201

  req.content_type = "text/plain"
  req.send_http_header()
  LogFunction('CreateUser',newuser.id, newuser.password)
  str = "user:%s\npassword:%s\n" % ( newuser.id, newuser.password)
  dbmobile_log.IP= "ooo"
  req.write( str )
  return apache.OK

def modifyuser(req,id=None,passwd=None,**params):
	dbmobile_log.IP= req.subprocess_env.get("REMOTE_ADDR")
	LogFunction('ModifyUser',id, passwd, **params)
	user = dbmobile_user.checkuser(id,passwd)

	if user is None:
		dbmobile_log.writeInLog(" Not exis", ErrorLevel.Err)
		return NOK

	else:
		for name in params.keys():
			if name == 'age':
				user.age = params[name]
			elif name == 'gender':
				user.gender = params[name]
			elif name == 'postal code':
				user.postal_code = params[name]

		dbmobile_user.modify(user)
		dbmobile_log.writeInLog(" Save", ErrorLevel.Log)
		return OK

def getuser(req,id=None):
	passwd=""
	user = dbmobile_user.checkuser(userid,passwd)
	if user is None:
		return 1
	
	req.content_type = "text/plain"
	req.send_http_header()
	str = "user:%s\npassword:%s\nip:%s\nbrowser:%s\ncreated:%s\n" % (user.id,user.password,user.source_ip,user.browser,user.created)
	req.write( str )
	return apache.OK

def createquestionnaire(req,id=None,passwd=None,**params):
	dbmobile_log.IP= req.subprocess_env.get("REMOTE_ADDR")
	LogFunction('CreateQuestionnaire',id, passwd, **params)

	user = dbmobile_user.checkuser(id,passwd)

	req.add_common_vars()
	user = dbmobile_user.checkuser(id,passwd)

	if user is None:
		dbmobile_log.writeInLog(" User doen't exists", ErrorLevel.Err)
		return NOK

	item = dbmobile_questionaire.init()

	if item is None:
		dbmobile_log.writeInLog(" Item doesn't create", ErrorLevel.Err)
		return NOK

	item.userid = user.id

	for name in params.keys():
		if name == 'step1':
			item.step1 = params[name]
		elif name == 'step2':
			item.step2 = params[name]
		elif name == 'step3':
			item.step3 = params[name]
		elif name == 'step4':
			item.step4 = params[name]
		elif name == 'step5':
			item.step5 = params[name]
		elif name == 'step6':
			item.step6 = params[name]
		elif name == 'step7':
			item.step7 = params[name]
		elif name == 'scale7shq':
			item.scale7shq = params[name]
		elif name == 'diener':
			item.diener = params[name]
		elif name == 'love':
			item.love = params[name]
		elif name == 'health':
			item.health = params[name]
		elif name == 'job':
		 item.job = params[name]

	item.source_ip = req.subprocess_env.get("REMOTE_ADDR")
	item.browser = req.subprocess_env.get("HTTP_USER_AGENT")

	dbmobile_questionaire.add(item)	
	dbmobile_log.writeInLog(" Save", ErrorLevel.Log)
	return OK

def createreminder(req,id=None,passwd=None,**params):
	dbmobile_log.IP= req.subprocess_env.get("REMOTE_ADDR")
	LogFunction('CreateReminder',id, passwd, **params)

	req.add_common_vars()
	req.add_common_vars()
	user = dbmobile_user.checkuser(id,passwd)
	if user is None:
		dbmobile_log.writeInLog(" User doen't exists", ErrorLevel.Err)
		return NOK

	item = dbmobile_reminder.init()
	item.userid = user.id

	for name in params.keys():
		if name == 'grade':
			item.grade = params[name]

	item.source_ip = req.subprocess_env.get("REMOTE_ADDR")
	item.browser = req.subprocess_env.get("HTTP_USER_AGENT")
	dbmobile_reminder.add(item)	
	dbmobile_log.writeInLog(" Save", ErrorLevel.Log)
	return OK

