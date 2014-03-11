'''
Created on 10 mar 2014

@author: mariusz
'''

import DOMElement


class DOMStructure(object):

    _tree = property(get_tree, set_tree, del_tree, "_tree's docstring")
    
    def __init__(self):
        self._tree = list()

    def get_tree(self):
        return self.__tree


    def set_tree(self, value):
        self.__tree = value


    def del_tree(self):
        del self.__tree
        
    def append_element(self, child):
        width = 
        self._tree.append(DOMElement())
        
    

    

def walker(soup, domStructure):
    
    if soup.name is not None:
        for child in soup.children:
            domStructure.append_element(child);
            walker(child)


def create_dom_structure(pageSoupSource):
    pass


