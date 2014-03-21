#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import hashlib
  
  
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
      
        
def create_dom_structure(html):
        
    return process_node(html, None)
 
 
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


def print_ast(ast, level=1):
    """
    Printing content of tree.
    """
    print ("\t"*level) + ast.xpath
    for child in ast.children:
        print_ast(child, level + 1)


def get_ast(url=None, driver=None):
    """
    Return an ast of webpage.
    """
    driver.get(url)
    html = driver.find_elements_by_xpath("child::*")
    dom = create_dom_structure(html[0])
    driver.close()
    return dom
 
 
 
def get_workarea(ast_list):
    """
    Analyze a given webpage and return xpath to a work area.
	"""
    result = list()
    
    for i in range(0, len(ast_list)):
        for j in range(i + 1, len(ast_list)):
            result = result + do_analysis(ast_list[i], ast_list[j])
                
    return result
