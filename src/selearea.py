#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from selenium import webdriver

class DOMElement(object):
    '''
    Representation of a single node.
    '''
    def __init__(self, width = None, height = None, md5 = None, x = None,
                y = None, xpath = None, parent = None, children = None):
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

    def print_all(self, level = 1):
        """
        Printing content of node.
        :param level: degree of the current subtree
        """
        print "\t" * level + self.xpath

        for child in self.children:
            child.print_all(level + 1)

def get_ast(url = None, driver = None):
    """
    This function return an ast of webpage. It is a tree that allows comparison of multiple websites.
    If a driver is provided, it will not be closed, otherwise, an webdriver.Firefox() will be used.

    :param url: url of webpage
    :param driver: selenium driver
    :return: tree of the webpage
    """

    def process_node(html, parent):
        """
        Processing single node.
        :param html: webelement from selenium to process
        :param parent: parent of given webelement
        :return: node in a tree
        """
        width = html.size['width']
        height = html.size['height']
        x = html.location['x']
        y = html.location['y']
        md5 = hashlib.md5(html.text.encode('utf-8')).hexdigest()

        xpath  = parent.xpath + "/" if parent != None else "//"
        xpath += str(html.tag_name)

        attribute = str(html.get_attribute("id"))
        if attribute != "":
            xpath = xpath + "[@id='" + attribute + "']"

        attribute = str(html.get_attribute("class"))
        if attribute != "":
            xpath = xpath + "[@class='" + attribute + "']"

        node = DOMElement(width, height, md5, x, y, xpath, parent, list())
        children = html.find_elements_by_xpath("child::*")

        for child in children:
            node.add_child(process_node(child, node))

        return node

    def check_url(url):
        """
        Check if the url is ok.

        :param url: url of a webpage
        :type url: str
        :return: url of a webpage
        :rtype: str
        """
        if url == None:
            raise ValueError("None is not an allowed value")

        if not isinstance(url, basestring):
            raise ValueError("It's not a url.")

        if not (url.startswith("http://") or url.startswith("https://") or url.startswith("file://")):
            raise ValueError("http, https or file protocol required")

        return url

    url = check_url(url)

    closedriver = False

    if driver == None:
        driver = webdriver.Firefox()
        closedriver = True

    driver.get(url)
    html = driver.find_elements_by_xpath("child::*")
    dom = process_node(html[0], None)

    if closedriver == True:
        driver.close()

    return dom

def get_workarea(ast_list):
    """
    Analyze a given webpage and return xpath to a work area.

    :param ast_list: list of trees
    :return: xpaths for elements which are different on the webpages
    """

    def are_different(node1, node2):
        """
        Check if nodes are different (check md5 sum and children of nodes).
        :param node1: first node to check if nodes are different
        :param node1: second node to check if nodes are different
        :return: true or false
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
        :param node1: first node for analysis
        :param node2: second node for analysis
        :return list of xpaths
        """
        result = list()

        for child1 in node1.children:
            for child2 in node2.children:
                if child1.xpath == child2.xpath and child1.md5 != child2.md5:
                    if are_different(child1, child2):
                        result.append(child1.xpath)
                    else:
                        result += do_analysis(child1, child2)

        return result

    result = list()
    for i, ast1 in enumerate(ast_list):
        for j, ast2 in enumerate(ast_list, start = i + 1):
            result = result + do_analysis(ast1, ast2)

    return list(set(result))
