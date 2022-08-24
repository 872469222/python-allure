#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
import yaml

import pytest

with open("data.yml","r",encoding="utf-8") as  f:
	# dataa=data.load(stream= f,Loader=yaml.FullLoader)
	dataa =	yaml.load(stream= f,Loader=yaml.FullLoader)
@pytest.mark.parametrize("caselist",dataa)
def test_case(caselist):
	print(caselist)
def test_add():
	return
def test_add1():
	return
def div():
	return