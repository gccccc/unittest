#!/usr/bin
#encoding:utf-8
import unittest
from sample2 import sample2
class test2(unittest.TestCase):
    def setUp(self):
        self.sample2 = sample2()
        print "Running."
    def tearDown(self):
        print "Run done."
    def testopenfile(self):
        self.assertRaises(IOError,self.sample2.openfile,'notexist.txt')
    def testprintNum(self):
        self.assertRaises(NameError,self.sample2.printNum)
