#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
import pytest


data = [
    (2,2,4),
    (3,4,12)
]

def add(a,b):
    return a * b

@pytest.mark.parametrize('a,b,expect',data)
class TestParametrize(object):
    def test_parametrize_1(self,a,b,expect):
        print('\n测试函数1测试数据为\n{}-{}'.format(a,b))
        assert add(a,b) == expect

    def test_parametrize_2(self,a,b,expect):
        print('\n测试函数2测试数据为\n{}-{}'.format(a,b))
        assert add(a,b) == expect

if __name__ == "__main__":
    pytest.main(["-s","aabbccpytest.py"])