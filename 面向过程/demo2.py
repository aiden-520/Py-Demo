def findsmall(arr):
    smallarr_list = arr[0]
    smallarr_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallarr_list:
            smallarr_list = arr[i]
            smallarr_index = i
    return smallarr_index

a = [1,6,4,8,5,7,8]
print(findsmall(a))


