#!/bin/env python
#encoding:utf-8

"""
binarySearch
"""

class BinarySearch(object):
    """
        binarySearch
        method:
            search(arr)
    """

    def search(self, arr, key):
        """
        :param arr: the array to be searched
        :param key: the value to be searched for
        :return: index of the search key
        """
        low = 0
        high = len(arr) - 1
        while low <= high:
            middle = (low + high) // 2
            middle_key = arr[middle]
            if middle_key < key:
                low = middle + 1
            elif middle_key > key:
                high = middle - 1
            else:
                return middle
        return -1


if __name__ == '__main__':
    bc = BinarySearch()
    arr = [1, 3, 4, 5, 6]
    key = 5
    ind = bc.search(arr, key)
    if ind != -1:
        print ("find the key:" + str(key) + "at the arr" + str(ind))

