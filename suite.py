#!/usr/bin
#encoding:utf-8
import unittest
from test1 import test1
from test2 import test2

#suite = unittest.TestSuite()
#suite.addTest(test1("testsum"))
#suite.addTest(test1("testmul"))
#或者如果所有的测试用例都是以test开头的时候 可以用以下的方法导入所有
suite1 = unittest.makeSuite(test1,"test")
suite2 = unittest.makeSuite(test2,"test")
suite = unittest.TestSuite((suite1,suite2))
runner = unittest.TextTestRunner()
runner.run(suite)
