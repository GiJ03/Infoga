#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

from lib.output import *
from urlparse import urlsplit

def checkTarget(target):
	o = urlsplit(target)
	if o.netloc == "":
		if 'www.' in o.path:
			return o.path.split('www.')[1]
		return o.path
	elif o.netloc != "":
		if 'www.' in o.netloc:
			return o.netloc.split('www.')[1]
		return o.netloc
	else:
		return target

def checkEmail(email):
	if '@' not in email:
		exit.__call__(warn('Invalid email: %s'%email))
	return email

def checkSource(source):
	list_source = ['all','ask','baidu','google','bing','dogpile','exalead','jigsaw','pgp','yahoo']
	if source not in list_source:
		exit.__call__(warn('Invalid search engine: %s'%source))
	return source

def checkVerbose(verb):
	verb = int(verb)
	if verb == 0:
		return 1
	elif verb == 1:
		return 1
	elif verb == 2:
		return 2
	else:
		return 3