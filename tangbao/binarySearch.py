#coding=utf-8
a = list()
i = 0
#接收list
while i==0: #接收用户list
    insert = input("输入数字：（以enter结束）")
    if insert!='':
        a.append(int(insert))

    else:
        break
a.sort() #list升序排序
print(a)
key = int(input("查找的key："))
low = 0
high = len(a)-1
#print(high)
while high>=low:
    mid = (high + low)//2
    midValue = a[mid]
    if a[mid]<key:
        if mid==len(a)-1:
            print("没有key,检索到list最大值")
            break
        elif a[mid+1]>key:
            print("没有key")
            break
        else:
            low = mid + 1
    elif a[mid]>key:
        if mid==0:
            print("没有key,检索到list最小值")
            break

        elif a[mid-1]<key:
            print("没有key")
            break
        else:
            high = mid - 1

    else:
        print("key位置：",mid)
        break
