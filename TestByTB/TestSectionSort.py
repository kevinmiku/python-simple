# coding=utf-8
import unittest
from tangbao import SectionSort
class SectionSortTest(unittest.TestCase):
    def setUp(self):
        print("Section sort test start~")
        self.ss = SectionSort.SectionSort()

    def tearDown(self):
        print("sectio sort over!")

    def test_case1(self):
        arr = [3, 5, 1, 10, 7, 13]
        self.assertEqual([1, 3, 5, 7, 10, 13], self.ss.sort(arr))

    def test_case2(self):
        arr = [31, 51, 1, 10, 7, 13]
        self.assertEqual([1, 7, 10, 13, 31, 51], self.ss.sort(arr))

if __name__ == '__main__':
    unittest.main()