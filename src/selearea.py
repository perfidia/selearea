#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DOMStructure import create_dom_structure


def get_ast(url = None, driver = None):

	xpath_html= "child::*"
	driver.get(url);
	html = driver.find_elements_by_xpath(xpath_html)
	
	return create_dom_structure(html[0], url)



def get_workarea(trees):
	"""
	Analyze a given webpage and return xpath to a work area.

	:param urls: list with urls
	:type urls: list
	:param webelements: list of webelements (from selenium)
	:type driver: list
	:return: xpath of work area
	"""

	pass
