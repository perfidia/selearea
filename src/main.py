#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selearea import get_ast
from selearea import get_workarea
from selearea import print_ast
from selenium import webdriver


if __name__ == "__main__":
    
    webpages = {"http://fc.put.poznan.pl", 
                "http://fc.put.poznan.pl/rekrutacja/post-powanie-kwalifikacyjne%2C29.html",
                "http://fc.put.poznan.pl/o-wydziale/witamy%2C39.html"}
    ast_list = list()

    for page in webpages:
        ast = get_ast(page, webdriver.Firefox())
#         print_ast(ast)
        ast_list.append( ast )
        
    workarea_list = list(set(get_workarea(ast_list)))
    
    for workarea in workarea_list:
        print workarea