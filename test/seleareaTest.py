'''
Created on 19 mar 2014

@author: mariusz
'''
import unittest
import sys
sys.path.append("../src")
from selearea import get_ast
from selearea import get_workarea


class seleareaTest(unittest.TestCase):

    ast_list = None

    def get_fc_pages(self):
        
        webpages = {"http://fc.put.poznan.pl", 
        "http://fc.put.poznan.pl/rekrutacja/post-powanie-kwalifikacyjne%2C29.html",
        "http://fc.put.poznan.pl/o-wydziale/witamy%2C39.html"}
        
        self.ast_list = list()
    
        for page in webpages:
            ast = get_ast(page)
            self.ast_list.append( ast )
            
    def get_fce_pages(self):
    
        webpages = {"http://www.bis.put.poznan.pl/", 
                "http://www.bis.put.poznan.pl/evPages/show/id/182"}
        
        self.ast_list = list()
    
        for page in webpages:
            ast = get_ast(page)
            self.ast_list.append( ast )


    def tearDown(self):
        pass
    
    
    def test_get_ast_fc_count(self):
         
        self.get_fc_pages()
        self.assertEqual(3, len(self.ast_list), "AssertionFailed: count for fc pages.")
        
        
    def test_get_workarea_fc_content(self):
        
        self.get_fc_pages()        
        workarea_list = get_workarea(self.ast_list)
        xpath = str("\\html[@id=''][@class='js']\\body[@id=''][@class='']\\div[@id='right'][@class='']\\div[@id='content'][@class='']")
        self.assertEqual(xpath, workarea_list[1], "AssertionFailed: xpaths for fc pages.")
        
    def test_get_ast_fce_count(self):
         
        self.get_fce_pages()
        self.assertEqual(2, len(self.ast_list), "AssertionFailed: count for fc pages.")
        
        
    def test_get_workarea_fce_content(self):
        
        self.get_fce_pages()        
        workarea_list = get_workarea(self.ast_list)
        xpath = str("\\html[@id=''][@class='']\\body[@id=''][@class='']\\div[@id='main'][@class='']\\div[@id=''][@class='']\\div[@id='left_menu'][@class='']\\div[@id='left_menu_box'][@class='']")
        self.assertEqual(xpath, workarea_list[0], "AssertionFailed: xpaths for fc pages.")
            

if __name__ == "__main__":
    unittest.main()