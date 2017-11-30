# coding=utf-8
"""

冒泡排序

"""
class BubbleSort(object):
    def sort(arr):
        i = 0
        j = 0
        for j in range(len(arr)-1):
            for i in range(len(arr)-1):
                #print i
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
        return arr
    if __name__ == '__main__':

        list1 = [11,0,33,55]
        print (sort(list1))