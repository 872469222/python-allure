#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
# 单个数据
import pytest


data = ["Rose","white"]

@pytest.mark.parametrize("name",data)
def test_parametrize(name):
    print('\n列表中的名字为\n{}'.format(name))

if __name__ == "__main__":
    pytest.main(["-s","test_07.py"])