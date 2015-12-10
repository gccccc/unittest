#!/usr/bin
#encoding:utf-8
import unittest
from sample1 import sample1
class test1(unittest.TestCase):
	def setUp(self):
                print 'Running.'
                self.sample1 = sample1()
        def tearDown(self):
                print "Run done."
	def testsum(self):
		self.assertEqual(self.sample1.sum(1,2),2,"test sum fail")
	        self.assertEqual(self.sample1.sum(2,3),5,"test sum fail")
        def testsub(self):
		self.assertEqual(self.sample1.sub(1,2),-1,"test sub fail")
	def testmul(self):
		self.assertEqual(self.sample1.mul(2,3),6,"test mul fail")
	def testdiv(self):
		self.assertEqual(self.sample1.div(4,2),2,"test div fail")
                self.assertEqual(self.sample1.div(2,0),0,"test div fail")
