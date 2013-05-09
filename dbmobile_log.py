import datetime
import time
import os

LOG_FOLDER = '/var/log/happyup'
LOG_FILENAME = 'happyup.log'
LOG_DEBUG = 1
IP=""

def enum(**enums):
		return type('Enum', (), enums)

ErrorLevel = enum(Log='LOG', Err='ERR', Warn='WARN')

def writeInLog(msg, level):  
  if LOG_DEBUG == 1:
		str_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
		f = open( os.path.join( LOG_FOLDER, LOG_FILENAME), "a")    
		f.write("%s\t%s\t%s:\t%s\n" % (IP,str_now,level,msg))
		f.close
  return;

if __name__ == "__main__":
		writeInLog("test", ErrorLevel.Err)

