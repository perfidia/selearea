#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selearea import get_ast, get_workareas

if __name__ == "__main__":
    urls = [
            "http://www.bis.put.poznan.pl/",
            "http://www.bis.put.poznan.pl/evPages/show/id/182"
    ]

    driver = webdriver.Firefox()

    asts = [get_ast(url, driver) for url in urls]

    for workarea in get_workareas(asts):
        print workarea

    driver.close()
