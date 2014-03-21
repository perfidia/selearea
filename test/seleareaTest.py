'''
Created on 19 mar 2014

@author: mariusz
'''
import unittest
from src.selearea import get_ast
from src.selearea import get_workarea
from selenium import webdriver

class Test(unittest.TestCase):

    ast_list = None

    def setUp(self):
        webpages = {"http://fc.put.poznan.pl", 
        "http://fc.put.poznan.pl/rekrutacja/post-powanie-kwalifikacyjne%2C29.html",
        "http://fc.put.poznan.pl/o-wydziale/witamy%2C39.html"}
        
        self.ast_list = list()
    
        for page in webpages:
            ast = get_ast(page, webdriver.Firefox())
            self.ast_list.append( ast )


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    
    def test_get_ast_count(self):
        
        self.assertEqual(3, len(self.ast_list), "msg")
        
        
    def test_get_workarea_fc_content(self):
        
        workarea_list = list(set(get_workarea(self.ast_list)))
        
        self.assertEqual("\html[@id=''][@class='js']\body[@id=''][@class='']\div[@id='right'][@class='']\div[@id='content'][@class='']", 
                         workarea_list[1], "msg")
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()