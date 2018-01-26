#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

from lib.color import *

class banner:
	def __ban__(self):
		print "_"*40
		print " Infoga - Email Information Gathering"
		print "       Momo Outaadi (m4ll0k)"
		print "     %shttps://github.com/m4ll0k%s"%(color().yellow,
			color().reset)
		print "_"*40
		print ""

	def __usage__(self,_exit_=False):
		self.__ban__()
		print "Usage: infoga.py [OPTIONS]\n"
		print "\t-d --domain\tTarget URL/Name"
		print "\t-s --source\tSource data (default \"all\"):\n"
		print "\t\tall\tUse all search engine"
		print "\t\tgoogle\tUse google search engine"
		print "\t\tbing\tUse bing search engine"
		print "\t\tyahoo\tUse yahoo search engine"
		print "\t\task\tUse ask search engine"
		print "\t\tbaidu\tUse baidu search engine"
		print "\t\tdogpile\tUse dogpile search engine"
		print "\t\texalead\tUse exalead search engine "
		print "\t\tjigsaw\tUse jigsaw search engine"
		print "\t\tpgp\tUse pgp search engine\n"
		print "\t-i --info\tGet email informations"
		print "\t-v --verbose\tVerbose level (1,2 or 3)"
		print "\t-h --help\tShow this help and exit\n"
		print "Example:"
		print "\tinfoga.py --domain site.gov -v 3"
		print "\tinfoga.py --info admin@site.gov -v 3"
		print "\tinfoga.py --domain site.gov --source google -v 3\n"
		if _exit_: exit.__call__()