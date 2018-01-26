#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

import urllib3
import requests
from lib.output import *

class Request:
	def __init__(self):
		pass
	agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
	def send(self,method,url,params=None,data=None,headers=None):
		if headers is None: headers = {}
		headers['User-Agent'] = Request.agent
		try:
			request = requests.Session()
			req = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
			req = request.request(
				method = method.upper(),
				url = url,
				params = params,
				data = data,
				allow_redirects = True,
				verify=False)
			return req
		except Exception,Error:
			exit(warn('Failed to establish a new connection'))
			
