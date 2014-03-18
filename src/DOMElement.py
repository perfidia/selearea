'''
Created on 09 mar 2014

@author: mariusz
'''

class DOMElement(object):
    '''
    classdocs
    '''
    def __init__(self, width=None, height=None,
                    md5=None, x=None, y=None, xpath=None, parent=None, children=None):
        self.__width = width
        self.__height = height
        self.__md5 = md5
        self.__x = x
        self.__y = y
        self.__xpath = xpath
        self._parent = parent
        self._children = children

    def get_parent(self):
        return self.__parent


    def get_children(self):
        return self.__children


    def set_parent(self, value):
        self.__parent = value


    def set_children(self, value):
        self.__children = value


    def del_parent(self):
        del self.__parent


    def del_children(self):
        del self.__children


    def get_width(self):
        return self.__width


    def get_height(self):
        return self.__height


    def get_md_5(self):
        return self.__md5


    def get_x(self):
        return self.__x


    def get_y(self):
        return self.__y


    def get_xpath(self):
        return self.__xpath


    def set_width(self, value):
        self.__width = value


    def set_height(self, value):
        self.__height = value


    def set_md_5(self, value):
        self.__md5 = value


    def set_x(self, value):
        self.__x = value


    def set_y(self, value):
        self.__y = value


    def set_xpath(self, value):
        self.__xpath = value


    def del_width(self):
        del self.__width


    def del_height(self):
        del self.__height


    def del_md_5(self):
        del self.__md5


    def del_x(self):
        del self.__x


    def del_y(self):
        del self.__y


    def del_xpath(self):
        del self.__xpath
        
        
    def get_degree(self):
        return len(self.get_children())
    
    
    def is_leaf(self):
        return (len(self.get_children()) == 0)
    
    
    def add_child(self, child):
        child.set_parent(self)
        self._children.append(child)
    
    
    def get_child(self, i):
        if i >= 0 and i < len(self._children):
            return self._children[i]
        else:
            return None
    
    _width = property(get_width, set_width, del_width, "_width's docstring")
    _height = property(get_height, set_height, del_height, "_height's docstring")
    _md5 = property(get_md_5, set_md_5, del_md_5, "_md5's docstring")
    _x = property(get_x, set_x, del_x, "_x's docstring")
    _y = property(get_y, set_y, del_y, "_y's docstring")
    _xpath = property(get_xpath, set_xpath, del_xpath, "_xpath's docstring")
    
    _parent = property(get_parent, set_parent, del_parent, "_parent's docstring")
    _children = property(get_children, set_children, del_children, "_children's docstring")
    
    
