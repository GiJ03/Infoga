#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

import sys
import json
import getopt

from lib.check import *
from lib.banner import *
from lib.output import *

from recon.ask import *
from recon.baidu import *
from recon.bing import *
from recon.dogpile import *
from recon.exalead import *
from recon.google import *
from recon.jigsaw import *
from recon.shodan import *
from recon.mailtester import *
from recon.pgp import *
from recon.yahoo import *

class infoga(object):
	""" infoga """
	def __init__(self):
		self.listEmail = []
		self.verbose = 1
		self.source = "all"
	
	def ask(self,target):
		emails = Ask(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Ask'%len(emails))

	def baidu(self,target):
		emails = Baidu(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Baidu'%len(emails))

	def bing(self,target):
		emails = Bing(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Bing'%len(emails))

	def dogpile(self,target):
		emails = Dogpile(target).search()
		if emails:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Dogpile'%(len(emails)))

	def exalead(self,target):
		emails = Exalead(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Exalead'%(len(emails)))

	def google(self,target):
		emails = Google(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Google'%(len(emails)))

	def jigsaw(self,target):
		emails = Jigsaw(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Jigsaw'%(len(emails)))

	def pgp(self,target):
		emails = PGP(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in PGP'%(len(emails)))

	def yahoo(self,target):
		emails = Yahoo(target).search()
		if emails != []:
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose == 2 or self.verbose == 3:
				info('Found %s emails in Yahoo'%(len(emails)))

	def shodan(self,ip):
		return Shodan(ip).search()

	def tester(self,email):
		return MailTester(email).search()

	def all(self,target):
		self.ask(target)
		self.baidu(target)
		self.bing(target)
		self.dogpile(target)
		self.exalead(target)
		self.google(target)
		self.jigsaw(target)
		self.pgp(target)
		self.yahoo(target)

	def main(self):
		if len(sys.argv) <= 2:
			banner().__usage__(True)
		try:
                        import argparse
                        parser = argparse.ArgumentParser()
                        parser.add_argument("-v","--verbose",help="verbose")
                        parser.add_argument("-s","--source",help="source")
                        
                        ## Only one of 'domain' or 'info' should be used at a time. ##
                        g = parser.add_mutually_exclusive_group()
                        g.add_argument("-d","--domain",help="domain")
                        g.add_argument("-i","--info",help="email")
                        args= parser.parse_args()
		except Exception,Error:
			banner().__usage__(True)
		banner().__ban__()

		#Arguments:
                self.verbose = checkVerbose(args.verbose)
                if args.source != None:
                        self.source = checkSource(args.source)
                else:
                        self.source = checkSource('all)
                if args.domain != None:
                        self.domain = checkTarget(args.domain)
                        # search
                        if self.source == "ask":self.ask(self.domain)
                        elif self.source == "all":self.all(self.domain)
                        elif self.source == "google":self.google(self.domain)
                        elif self.source == "baidu":self.baidu(self.domain)
                        elif self.source == "bing":self.bing(self.domain)
                        elif self.source == "dogpile":self.dogpile(self.domain)
                        elif self.source == "exalead":self.exalead(self.domain)
                        elif self.source == "jigsaw":self.jigsaw(self.domain)
                        elif self.source == "pgp":self.pgp(self.domain)
                        elif self.source == "yahoo":self.yahoo(self.domain)
                if args.info != None:
                        self.listEmail.append(checkEmail(args.info))
                        test('Checking info for "%s"'%(args.info)) 
		
		if self.listEmail == []:
			exit(warn('Not found emails :('))
		for email in self.listEmail:
			ip = self.tester(email)
			for i in ip:
				data(i,json.loads(self.shodan(i)),email,self.verbose)

if __name__ == "__main__":
	try:
		infoga().main()
	except KeyboardInterrupt,Error:
		exit(warn("CTRL+C, :("))
