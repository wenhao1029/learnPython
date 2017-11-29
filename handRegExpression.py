#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def checkIfEmailFormat(emailAddress):
	p=r'[a-zA-Z0-9\_\.]+@[a-zA-Z0-9]+\.com'
	return re.match(p,emailAddress)


if (__name__ == '__main__'):
	emailAddress = "toby.wang@ericson.com"
	if checkIfEmailFormat(emailAddress):
		print("It's valid email address!")
	else:
		print("It's not valid email address!")