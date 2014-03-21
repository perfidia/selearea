#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selearea import get_ast
from selenium import webdriver
from DOMStructure import *

ast = get_ast("http://fc.put.poznan.pl", webdriver.Firefox())
ast2 = get_ast("http://fc.put.poznan.pl/rekrutacja/post-powanie-kwalifikacyjne%2C29.html", webdriver.Firefox())

dict = do_analysis(ast.get_root_node(), ast2.get_root_node())
 
print "ok"