#-*- coding: utf-8 -*-
'''
Created on 23 mar 2014

@author: mariusz
@author: tomasz
'''

import unittest
from selearea import get_ast, get_workareas

class seleareaTest(unittest.TestCase):
    def get_fc_pages(self):
        urls = {
                "http://fc.put.poznan.pl",
                "http://fc.put.poznan.pl/rekrutacja/post-powanie-kwalifikacyjne%2C29.html",
                "http://fc.put.poznan.pl/o-wydziale/witamy%2C39.html"
        }

        return [get_ast(url) for url in urls]

    def get_fce_pages(self):
        urls = {
                "http://www.bis.put.poznan.pl/",
                "http://www.bis.put.poznan.pl/evPages/show/id/182"
        }

        return [get_ast(url) for url in urls]

    def get_identical_pages(self):
        urls = {
                "http://www.bis.put.poznan.pl/",
                "http://www.bis.put.poznan.pl/"
        }

        return [get_ast(url) for url in urls]

    def test_get_wrong_page(self):
        url = "putpoznan.pl"

        with self.assertRaises(ValueError):
            get_ast(url)

    def test_get_none_page(self):
        with self.assertRaises(ValueError):
            get_ast(None)

    def test_get_workarea_identical_pages(self):
        asts = self.get_identical_pages()
        workareas = get_workareas(asts)
        self.assertEqual(0, len(workareas), "AssertionFailed: work area found on identical pages.")

    def test_get_ast_fc_count(self):
        asts = self.get_fc_pages()
        self.assertEqual(3, len(asts), "AssertionFailed: count for fc pages.")

    def test_get_workarea_fc_content(self):
        asts = self.get_fc_pages()
        workareas = get_workareas(asts)
        xpath = str("//html[@class='js']/body/div[@id='right']/div[@id='content']")
        self.assertEqual(xpath, workareas[0], "AssertionFailed: xpaths for fc pages.")

    def test_get_ast_fce_count(self):
        asts = self.get_fce_pages()
        self.assertEqual(2, len(asts), "AssertionFailed: count for fc pages.")

    def test_get_workarea_fce_content(self):
        asts = self.get_fce_pages()
        workareas = get_workareas(asts)
        xpath = str("//html/body/div[@id='main']/div/div[@id='left_menu']/div[@id='left_menu_box']")
        self.assertEqual(xpath, workareas[1], "AssertionFailed: xpaths for fc pages.")

if __name__ == "__main__":
    unittest.main()
