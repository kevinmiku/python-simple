# coding=utf-8
import unittest
from tangbao import BubbleSort
class TestBubble(unittest.TestCase):
    def setUp(self):
        self.bs = BubbleSort.BubbleSort()
        print("Test BubbleSort start~")

    def tearDown(self):
        print("Bubble Sort test over!")

    def test_case1(self):
        arr = [9, 1, 4, 6, 3, 10]
        self.assertEqual([1, 3, 4, 6, 9, 10], self.bs.sort(arr))

    def test_case2(self):
        arr = [4, 6, 3, 10]
        self.assertEqual([3, 4, 6, 10], self.bs.sort(arr))

    def test_case3(self):
        arr = [4]
        self.assertEqual([4], self.bs.sort(arr))

if __name__ == '__main__':
    unittest.main()
