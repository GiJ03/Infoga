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

class Yahoo(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Yahoo...'%(self.target))
		url = "http://search.yahoo.com/search?p=%40{}&b=0&pz=10".format(self.target)
		try:
			resp = self.send(
				method = "GET",
				url = url,
				headers = {
							'Host':'search.yahoo.com'
							}
				)
			return self.getmail(resp.content,self.target)
		except Exception,Error:
			pass

	def getmail(self,content,target):
		return parser(content,target).email()