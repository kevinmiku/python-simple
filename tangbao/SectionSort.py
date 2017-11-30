# coding=utf-8
"""
选择排序

"""
class SectionSort():
    def sort(self, arr):
        j = 0
        for j in range(len(arr)-1):
            i = j
            index = i
            for i in range(len(arr)-1)[i:]:
                if arr[index]>arr[i+1]:
                    index = i + 1
            arr[j], arr[index] = arr[index], arr[j]
        return arr
if __name__ == '__main__':
    array = [3, 1, 6, 9, 11, 0]
    ss = SectionSort()
    print(ss.sort(array))