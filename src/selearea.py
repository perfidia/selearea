#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from lxml import *
import urllib2
import hashlib



def get_md5(text = None):
	
	print hashlib.md5(text).hexdigest()


#TODO: find a way to get a xpath for single element and generate nodes
def get_ast(url = None, driver = None):
	
# 	location = webelement.location
# 	size = webelement.size
# 	pageSource = urllib2.urlopen(url)
# 	pageSoupSource = BeautifulSoup(pageSource.read())
# 	print pageSoupSource
	pageSource = driver.get(url);
	pageSoupSource = BeautifulSoup(pageSource)
	createDOMStructure(pageSoupSource)


def get_workarea(urls = None, webelements = None):
	"""
	Analyze a given webpage and return xpath to a work area.

	:param urls: list with urls
	:type urls: list
	:param webelements: list of webelements (from selenium)
	:type driver: list
	:return: xpath of work area
	"""

	pass
