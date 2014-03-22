#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import hashlib
from selenium import webdriver
  
class DOMElement(object):
    '''
    Representation of a single node.
    '''
    width = None
    height = None
    md5 = None
    x = None
    y = None
    xpath = None
    parent = None
    children = None
       
    def __init__(self, width=None, height=None,
                    md5=None, x=None, y=None, xpath=None, parent=None, children=None):
        self.width = width
        self.height = height
        self.md5 = md5
        self.x = x
        self.y = y
        self.xpath = xpath
        self.parent = parent
        self.children = children
    
       
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def print_all(self, level=1):
        """
        Printing content of node.
        """
        print ("\t"*level) + self.xpath
        for child in self.children:
            child.print_all(level + 1)
           
           
def get_ast(url=None, driver=None):
    """
    Return an ast of webpage.
    """
    
    def process_node(html, parent):
        """
        Processing single node.
        """
        width = html.size['width']
        height = html.size['height']
        x = html.location['x']
        y = html.location['y']
        md5 = hashlib.md5(html.text).hexdigest()
        xpath = ""
           
        if parent != None:
            xpath = parent.xpath
               
        xpath = xpath + "\\" + str(html.tag_name) + "[@id='" + str(html.get_attribute("id")) + "'][@class='" + str(html.get_attribute("class")) + "']"
           
        node = DOMElement(width, height, md5, x, y, xpath, parent, list())
        children = html.find_elements_by_xpath("child::*")
       
        for child in children:
            node.add_child(process_node(child, node))
               
        return node
    
    def check_url(url):
        if not isinstance(url, basestring):
            raise ValueError("It's not a url.")

        if url[:7] != "http://" and url[:8] != "https://":
            raise ValueError("http or https protocol is required")

        return url
    
    url = check_url(url)
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.find_elements_by_xpath("child::*")
    dom = process_node(html[0], None)
    driver.close()
    
    return dom
 
 
 
def get_workarea(ast_list):
    """
    Analyze a given webpage and return xpath to a work area.
	"""
    
    def are_different(node1, node2):
        """
        Check if nodes are different.
        """
        different_children = True
        for child1 in node1.children:
            for child2 in node2.children:
                if child1.md5 == child2.md5:
                    different_children = False
    
        return different_children

    
    def do_analysis(node1, node2):
        """
        Analysis of pairs of nodes.
        """
        result = list()
         
        for child1 in node1.children:
            for child2 in node2.children:
                if child1.xpath == child2.xpath and child1.md5 != child2.md5:
                    if are_different(child1, child2):
                        result.append(child1.xpath)
                    else:
                        result = result + do_analysis(child1, child2)
                
        return result
    
    
    result = list()
    for i, ast1 in enumerate(ast_list):
        for j, ast2 in enumerate(ast_list, start=i+1):
            result = result + do_analysis(ast1, ast2)
                
    return list(set(result))
