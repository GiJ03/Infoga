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

class Baidu(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Baidu...'%(self.target))
		url = "http://www.baidu.com/s?wd=%40{}&pn=0".format(self.target)
		try:
			resp = self.send(
				method = "GET",
				url = url,
				headers = {
							'Host':'www.baidu.com'
							}
				)
			return self.getmail(resp.content,self.target)
		except Exception,Error:
			pass

	def getmail(self,content,target):
		return parser(content,target).email()
