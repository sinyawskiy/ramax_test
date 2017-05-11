#!/usr/bin/python
# -*- coding: utf-8 -*-

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class Parent(object):
    def __init__(self, param=None):
        if param is not None:
            self.i = param
        else:
            self.i = 3
    def get_isSecond(self):
        return isinstance(self, Second)
    def set_isSecond(self, value):
        raise AttributeError
    isSecond = property(get_isSecond, set_isSecond)
    def isFirst(self):
        return isinstance(self, First)
    def fnc(self, param_1, param_2=None):
        if param_2 is None:
            if param_1 == 7:
                raise MyError('Error text')
            return param_1*param_1*self.i
        else:
            return param_1*param_2*self.i

class First(Parent):
    pass

class Second(Parent):
    pass
    
class A(First):
    pass
