# coding=utf-8
class MergeSort():
    def MergeSort(self, arr, first, last):
        self.ms = MergeSort()
        if first < last:
            middle = (last + first) // 2
            self.ms.MergeSort(arr, first, middle)
            self.ms.MergeSort(arr, middle + 1, last)
            self.ms.Merge(arr, first, middle, last)
        return arr


    def Merge(self, arr, first, middle, last):
        len1 = len(arr[first: middle + 1])
        len2 = len(arr[middle + 1:last + 1])
        n = last - middle
        list1 = []   #存放列表
        list2 = []
        for i in range(len1):
            list1.append(arr[i + first])
        for j in range(len2):
            list2.append(arr[middle + j + 1])
        i = 0
        j = 0
        for k in range(len(arr))[first:last+1]:
            if i < len(list1) and j < len(list2):
                if list1[i] <= list2[j]:
                    arr[k] = list1[i]
                    i += 1
                elif list1[i] > list2[j]:
                    arr[k] = list2[j]
                    j += 1
            elif j < len(list2):
                arr[k] = list2[j]
                j += 1
            elif i < len(list1):
                arr[k] = list1[i]
                i += 1

if __name__ == '__main__':
    ms = MergeSort()
    array = [4, 1, 3, 2, 9, 8]
    last = len(array) - 1

    print(ms.MergeSort(array, 0, last))

