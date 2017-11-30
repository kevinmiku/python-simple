# coding=utf-8
import  unittest
"""
by tangbao

运行binarySearchTest.py里的测试用例

"""
from test import TestBinarySearchByTB
#定义一个测试集合管理case
def suite1():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestBinarySearchByTB.TestBS("test_case1"))
    suiteTest.addTest(TestBinarySearchByTB.TestBS("test_case2"))
    return suiteTest
def suite2():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestBinarySearchByTB.TestBS("test_case1"))
    suiteTest.addTest(TestBinarySearchByTB.TestBS("test_case2"))
    return suiteTest
def AllSuite():
    allTest = unittest.TestSuite((suite1(),suite2()))
    return allTest
if __name__ == '__main__':
    #通过一个测试集合管理case 运行两种方案
    #第一种
    # runner = unittest.TextTestRunner()
    # runner.run(suite1())
    #第二种
    #unittest.main(defaultTest='suite1')

    #多个测试集合运用
    runner = unittest.TextTestRunner()
    runner.run(AllSuite())




