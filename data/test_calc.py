#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
from calc import Calculator
import yaml
import pytest
import allure


with open('calc_list.yaml', 'r', encoding='utf-8') as f:
    datas = yaml.safe_load(f)['calc_case']
    add_list = datas['add_list']  # 加法测试用例
    sub_list = datas['sub_list']  # 减法测试用例
    mul_list = datas['mul_list']  # 乘法测试用例
    div_list = datas['div_list']  # 除法测试用例
    ids = datas['all_ids']  # 全部的标签
    print(datas)


@allure.feature("计算器模块")
class TestCalc:
    def setup_class(self):
        print("计算器开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算器结束计算")

    @allure.story("加法运算")
    @pytest.mark.parametrize("a, b, expect", add_list, ids=ids)
    def test_add(self, a, b, expect):
        with allure.step(f"输入测试用例{a}, {b}, 预期结果为{expect}"):
            result = self.calc.add(a, b)
            if isinstance(result, float):  # 判断浮点数
                result = round(result, 2)
        assert expect == result

    @allure.story("减法运算")
    @pytest.mark.parametrize("a, b, expect", sub_list, ids=ids)
    def test_sub(self, a, b, expect):
        with allure.step(f"输入测试用例{a}, {b}, 预期结果为{expect}"):
            result = self.calc.sub(a, b)
            if isinstance(result, float):  # 判断浮点数
                result = round(result, 2)
        assert expect == result

    @allure.story("乘法运算")
    @pytest.mark.parametrize("a, b, expect", mul_list, ids=ids)
    def test_mul(self, a, b, expect):
        with allure.step(f"输入测试用例{a}, {b}, 预期结果为{expect}"):
            result = self.calc.mul(a, b)
            if isinstance(result, float):  # 判断浮点数
                result = round(result, 2)
        assert expect == result

    @allure.story("除法运算")
    @pytest.mark.parametrize("a, b, expect", div_list, ids=ids)
    def test_div(self, a, b, expect):
        with allure.step(f"输入测试用例{a}, {b}, 预期结果为{expect}"):
            result = self.calc.division(a, b)
            if isinstance(result, float):  # 判断浮点数
                result = round(result, 2)
        assert expect == result


if __name__ == '__main__':
    # pytest.main(["-vs", "test_calc.py::TestCalc::test_div"])  # 不需要allure的时候执行, 指定某个测试用例
    pytest.main(["--alluredir=result/2", "test_calc.py"])  # 生成allure
    # 查看allure用例 allure serve .\result\2\
