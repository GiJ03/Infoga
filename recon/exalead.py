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

class Exalead(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Exalead...'%(self.target))
		url = "http://www.exalead.com/search/web/results/?q=%40{}&elements_per_page=50&start_index=0".format(self.target)
		try:
			resp = self.send(
				method = "GET",
				url = url,
				headers = {
							'Host':'www.exalead.com',
							'Referer':'http://exalead.com/search/web/results/?q=%40{}'.format(self.target)
							}
				)
			return self.getmail(resp.content,self.target)
		except Exception,Error:
			pass

	def getmail(self,content,target):
		return parser(content,target).email()