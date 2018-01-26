#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

import re
import string

class parser:
	def __init__(self,content,target):
		self.target = target
		self.content = content

	def email(self):
		temp_email = re.findall(r'[a-zA-Z0-9.\-_+#~!$&\',;=:]+'+'@'+r'[a-zA-Z0-9.-]*'+self.target,self.clean())
		email_list = []
		for _email_ in temp_email:
			if _email_ not in email_list:
				email_list.append(_email_)
		return email_list

	def clean(self):
		self.content = re.sub('<em>','',self.content)
		self.content = re.sub('<b>','',self.content)
		self.content = re.sub('</b>','',self.content)
		self.content = re.sub('</em>','',self.content)
		self.content = re.sub('<strong>','',self.content)
		self.content = re.sub('</strong>','',self.content)
		self.content = re.sub('<wbr>','',self.content)
		self.content = re.sub('</wbr>','',self.content)
		for x in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
			self.content = string.replace(self.content,x,' ')
		return self.content