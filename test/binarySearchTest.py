import unittest

from hexie import binarySearch

class TestBinarySearch(unittest.TestCase):
    """ test binary search
    """
    def setUp(self):
        self.bs = binarySearch.BinarySearch()

    def test_common_arr(self):
        arr = [1, 3, 4, 5, 6]
        key = 5
        self.assertEqual(3, self.bs.search(arr, key))

    def test_unfind(self):
        self.bs = binarySearch.BinarySearch()
        arr = [1, 3, 4, 5, 6]
        key = 9
        self.assertEqual(-1, self.bs.search(arr, key))

if __name__ == '__main__':
    unittest.main()
