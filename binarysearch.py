def binarysearch(arr , target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
            return -1
arr = [12, 23, 45,66, 89]
target = 66
print(binarysearch(arr , target))
