#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

from lib.color import *

c = color()

def plus(string):
	print "%s[+]%s %s"%(c.green,c.reset,string)

def warn(string):
	print "%s[!]%s %s"%(c.red,c.reset,string)

def test(string):
	print "%s[*]%s %s"%(c.blue,c.reset,string)

def info(string):
	print "%s[i]%s %s"%(c.yellow,c.reset,string)

def more(string):
	print " %s|%s  %s"%(c.white,c.reset,string)

def data(ip,data,email,verbose):
	if verbose == 1:
		plus('Email: %s (%s)'%(email,ip))
	elif verbose == 2:
		try:
			plus('Email: %s (%s)'%(email,ip))
			if data['hostnames']:
				more('Hostname: %s'%(data['hostnames'][0]))
			if data['country_code'] and data['country_name']:
				more('Country: %s (%s)'%(data['country_code'],data['country_name']))
			if data['city'] and data['region_code']:
				more('City: %s (%s)'%(data['city'],data['region_code']))
		except KeyError,Error:
			pass
	elif verbose == 3:
		try:
			plus('Email: %s (%s)'%(email,ip))
			if data['hostnames']:more('Hostname: %s'%(data['hostnames'][0]))
			if data['country_code'] and data['country_name']:more('Country: %s (%s)'%(data['country_code'],data['country_name']))
			if data['city'] and data['region_code']:more('City: %s (%s)'%(data['city'],data['region_code']))
			if data['asn']: more('ASN: %s'%(data['asn']))
			if data['isp']: more('ISP: %s'%(data['isp']))
			if data['latitude'] and data['longitude']:
				more('Map: https://www.google.com/maps/@%s,%s,10z (%s,%s)'%(data['latitude'],
					data['longitude'],data['latitude'],data['longitude']))
			if data['org']: more('Organization: %s'%(data['org']))
			if data['ports']: more('Ports: %s'%(data['ports']))
			if data['vulns']: more('Vulnerability: %s'%(data['vulns']))
		except KeyError,Error:
			pass