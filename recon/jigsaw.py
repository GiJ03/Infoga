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

class Jigsaw(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Jigsaw...'%(self.target))
		url = "http://www.jigsaw.com/FreeTextSearch.xhtml?opCode=search&autoSuggested=True&freeText={}".format(self.target)
		try:
			resp = self.send(
				method = "GET",
				url = url
				)
			return self.getmail(resp.content,self.target)
		except Exception,Error:
			pass

	def getmail(self,content,target):
		return parser(content,target).email()