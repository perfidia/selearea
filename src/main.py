#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selearea import get_ast
from selenium import webdriver
from DOMStructure import get_leafs

ast = get_ast("http://fc.put.poznan.pl", webdriver.Firefox())

print "ok"