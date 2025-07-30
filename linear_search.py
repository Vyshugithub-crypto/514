def linearsearch(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1
        return -1
arr = [12, 33, 56, 67, 98]
target = 56
print(linearsearch(arr , target))
