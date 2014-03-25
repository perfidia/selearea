#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selearea import get_ast
from selearea import get_workarea
from selenium import webdriver

if __name__ == "__main__":
    
    webpages = {"http://www.bis.put.poznan.pl/", 
                "http://www.bis.put.poznan.pl/evPages/show/id/182"}
        
    ast_list = list()

    for page in webpages:
        ast = get_ast(page, webdriver.Firefox())
        ast_list.append( ast )
    
    for workarea in get_workarea(ast_list):
        print workarea