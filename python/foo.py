#!/usr/bin/env python
#! -*- coding: utf-8 -*-

"""
类方法、静态方法和实例方法的区别
"""

class Foo(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        pass


f = Foo()
f.m1(1)
f.m2(1)
f.m3(1)

