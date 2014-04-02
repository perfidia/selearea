'''
Created on 1 Apr 2014

@author: perf
'''
import unittest
import os
import selearea
from selenium import webdriver

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.getcwd().split(os.sep)

        for d in reversed(path[:]):
            if d != 'selearea':
                path.pop()
                continue

            break

        path.append("tests")
        path.append("www")

        cls.path = "file://" + os.sep.join(path)

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        try:
            self.driver.close()
        except:
            pass

    def getUrl(self, filename):
        return self.path + os.sep + filename

    def testDriver(self):
        """
        https://github.com/perfidia/selearea/issues/1
        """
        selearea.get_ast(self.getUrl("simple.html"), driver = self.driver)

        self.assertEqual(len(self.driver.find_elements_by_id("a")), 1)

    def testCheckCorrectnessOfXPaths(self):
        """
        https://github.com/perfidia/selearea/issues/3
        """
        urls = [
                "http://www.bis.put.poznan.pl/",
                "http://www.bis.put.poznan.pl/evPages/show/id/182"
        ]

        asts = []

        for url in urls:
            asts.append(selearea.get_ast(url, driver = self.driver))

        xpaths = selearea.get_workarea(asts)

        self.driver.get(urls[0])

        for xpath in xpaths:
            self.assertIsNotNone(self.driver.find_element_by_xpath(xpath))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
