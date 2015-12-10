#!/usr/bin
#encoding:utf-8

class sample2:
    def openfile(self,filename):
        try:
            open(filename,'r+')
        except IOError:
            return IOError

    def printNum(self):
        try:
            print notexist
        except NameError:
            return NameError

s = sample2()
res = s.openfile('notexist')
print res
