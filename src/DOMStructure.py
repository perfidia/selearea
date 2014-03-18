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
    
    if parent != None:
        xpath = parent.get_xpath() + "\\" + str(html.tag_name)
    else:
        xpath = "\\" + str(html.tag_name)
    
    node = DOMElement(width, height, md5, x, y, xpath, parent, list())
    xPathToGetChildren = "child::*"
    children = html.find_elements_by_xpath(xPathToGetChildren)

    for child in children:
        node.add_child(process_node(child, node))
        
    return node


def create_dom_structure(html, webpage_name):
    
    dom_structure = DOMStructure();
    root = process_node(html, None)
    dom_structure.set_root_node(root)
    dom_structure.set_webpage_name(webpage_name)
    
    return dom_structure


def get_leafs(root):
    
    out = list()
    
    for child in root.get_children():
        if child.is_leaf():
            out.append(child)
        else:
            out = list(set(out + get_leafs(child)))
            
    return out


# def compare_trees(tree1, tree2):
# 
#     children_tree1 = tree1.get_children()
#     children_tree2 = tree2.get_children()
#     out_tree1 = dict()
#     out_tree2 = dict()
#     
#     for child_tree1 in children_tree1:
#         for child_tree2 in children_tree2:
#             if child_tree1.get_md_5() != child_tree2.get_md_5():
#                 out_tree1.update({tree1.get_webpage_name() : child_tree1.get_xpath()})
#                 out_tree2.update({tree2.get_webpage_name() : child_tree2.get_xpath()})

def are_nodes_equals(node1, node2):
    pass


def compare_nodes(node1, node2):
    
    same_counter = 0
    
    for child1 in node1.get_children():
        for child2 in node2.get_children():
            if are_nodes_equals(child1, child2):
                same_counter =+ 1
                
    if same_counter == 0:
        return None
    else:
        return node1.get_parent().get_xpath()
    
    
def compare_trees(tree1, tree2):
    
    children_counter = len(tree1.get_children())
    
    for i in range(0, children_counter):
        if not are_nodes_equals(tree1.get_child(i), tree2.get_child(i)):
            comparison = compare_nodes(tree1.get_child(i), tree2.get_child(i))
            if comparison != None:
                pass





