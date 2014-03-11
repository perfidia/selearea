'''
Created on 09 mar 2014

@author: mariusz
'''

class DOMElement(object):
    '''
    classdocs
    '''
    
    _width = property(get_width, set_width, del_width, "_width's docstring")
    _height = property(get_height, set_height, del_height, "_height's docstring")
    _md5 = property(get_md_5, set_md_5, del_md_5, "_md5's docstring")
    _x = property(get_x, set_x, del_x, "_x's docstring")
    _y = property(get_y, set_y, del_y, "_y's docstring")
    _xpath = property(get_xpath, set_xpath, del_xpath, "_xpath's docstring")

    def __init__(self, width, height, md5, x, y, xpath):
        self.__width = width
        self.__height = height
        self.__md5 = md5
        self.__x = x
        self.__y = y
        self.__xpath = xpath

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
    
    