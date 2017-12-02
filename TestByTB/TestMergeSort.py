# coding=utf-8
import unittest
from tangbao import MergeSort
class MergeSortTest(unittest.TestCase):
    def setUp(self):
        print("Test Merge Sort start~")
        self.ms = MergeSort.MergeSort()

    def tearDown(self):
        print("Test Merge Sort over")

    def test_case1(self):
        array = [5]
        self.assertEqual([5], self.ms.MergeSort(array, 0, 0))

    def test_case2(self):
        array = [4, 1, 7, 2]
        self.assertEqual([1, 2, 4, 7], self.ms.MergeSort(array, 0, 3))

    def test_case3(self):
        array = [4, 1, 7, 2, 10, 9]
        self.assertEqual([1, 2, 4, 7, 9, 10], self.ms.MergeSort(array, 0, 5))

if __name__ == '__main__':
        unittest.main()