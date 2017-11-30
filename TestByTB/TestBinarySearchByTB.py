# coding=utf-8
import unittest
from tangbao import binarySearch2
"""
by tangbao

运行case在Suite.py文件

"""
class TestBS(unittest.TestCase):
    #测试用例执行前
    def setUp(self):
        print("test start!")
        self.bs = binarySearch2.BinarySearch()

    #测试用例执行后
    def tearDown(self):
        print("test down")

    def test_case1(self):
        arry = [4, 6, 7]
        key = 6
        self.assertEqual(1, self.bs.search(arry, key))

    def test_case2(self):
        array = [1]
        key = 0
        self.assertEqual(-1,self.bs.search(array, key))

