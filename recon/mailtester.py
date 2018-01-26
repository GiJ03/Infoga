#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

from lib.output import *
from lib.request import *
from lib.parser import *

class MailTester(Request):
	def __init__(self,email):
		Request.__init__(self)
		self.email = email

	def search(self):
		data = {'lang':'en'}
		data['email'] = self.email
		url = "http://mailtester.com/testmail.php"
		try:
			resp = self.send(
				method = "POST",
				url = url,
				data = data
				)
			return self.getip(resp.content)
		except Exception,Error:
			pass

	def getip(self,content):
		temp_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',content,re.I)
		list_ip = []
		for ip in temp_ip:
			if ip not in list_ip:
				list_ip.append(ip)
		return list_ip