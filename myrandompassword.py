#!/usr/bin/python
# Filename : myrandompassword.py

import string
import hashlib
import random

def generator(size=20, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def md5(str):
    return hashlib.sha224(str).hexdigest() 

version = '0.1'
# End of myrandompassword.py

