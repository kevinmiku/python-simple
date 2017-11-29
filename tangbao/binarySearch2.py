#coding=utf-8
class BinarySearch(object):
    def search(a,key):
        low = 0
        high = len(a) - 1
        # print(high)
        while high >= low:
            mid = (high + low) / 2
            midValue = a[mid]
            if a[mid] < key:
                if mid == len(a) - 1:
                    print("没有key,检索到list最大值")
                    break
                elif a[mid + 1] > key:
                    print("没有key")
                    break
                else:
                    low = mid + 1
            elif a[mid] > key:
                if mid == 0:
                    print("没有key,检索到list最小值")
                    break

                elif a[mid - 1] < key:
                    print("没有key")
                    break
                else:
                    high = mid - 1

            else:
                #print("key位置：", mid)
                return mid
        return -1

    if __name__ == '__main__':
        a = [1, 3, 7, 8, 10, 12]
        key = 8
        a.sort()  # list升序排序
        result = search(a,key)
        if result != -1:
            print ("key位置：",result)
