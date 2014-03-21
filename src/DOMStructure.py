'''
Created on 10 mar 2014

@author: mariusz
'''

from DOMElement import *
import hashlib


class DOMStructure(object):

    def __init__(self):
        pass

    def get_webpage_name(self):
        return self.__webpage_name


    def set_webpage_name(self, value):
        self.__webpage_name = value


    def del_webpage_name(self):
        del self.__webpage_name


    def get_root_node(self):
        return self.__root_node


    def set_root_node(self, value):
        self.__root_node = value


    def del_root_node(self):
        del self.__root_node
    
        
    _root_node = property(get_root_node, set_root_node, del_root_node, "_root_node's docstring")
    _webpage_name = property(get_webpage_name, set_webpage_name, del_webpage_name, "_webpage_name's docstring")
    

def process_node(html, parent):
    
    width = html.size['width']
    height = html.size['height']
    x = html.location['x']
    y = html.location['y']
    md5 = hashlib.md5(html.text).hexdigest()
    xpath = ""
    
    if parent != None:
        xpath = parent.get_xpath()
        
    xpath = xpath + "\\"+ str(html.tag_name) + "[@id='" + str(html.get_attribute("id"))  + "'][@class='" + str(html.get_attribute("class")) + "']"
    
    node = DOMElement(width, height, md5, x, y, xpath, parent, list())
    children = html.find_elements_by_xpath("child::*")

    for child in children:
        node.add_child(process_node(child, node))
        
    return node


def create_dom_structure(html, webpage_name):
    
    dom_structure = DOMStructure();
    root = process_node(html, None)
    dom_structure.set_root_node(root)
    dom_structure.set_webpage_name(webpage_name)
    
    return dom_structure


def are_different(node1, node2):
    
    different_children = True
    for child1 in node1.get_children():
        for child2 in node2.get_children():
            if child1.get_md_5() == child2.get_md_5():
                different_children = False

    return different_children

    
def do_analysis(node1, node2):
     
    result = list()
     
    for child1 in node1.get_children():
        for child2 in node2.get_children():
            if child1.get_xpath() == child2.get_xpath() and child1.get_md_5() != child2.get_md_5():
                if are_different(child1, child2):
                    result.append(child1.get_xpath())
                else:
                    result = result + do_analysis(child1, child2)
            
    return result


