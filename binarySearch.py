def binarySearch(arr, key) -> int: # iterative
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            hi = mid - 1
        elif arr[mid] < key:
            lo = mid + 1
    return -1

def recBinarySearch(arr, key, lo, hi) -> int: # recursive
    if lo > hi:
        return -1
    
    mid = (lo+hi) // 2
    if arr[mid] == key:
        return key
    if key < arr[mid]:
        return recBinarySearch(arr, key, lo, mid-1)
    elif arr[mid] < key:
        return recBinarySearch(arr, key, mid+1, hi)


# arr = [1, 2, 4, 5, 7, 8, 20, 20, 221, 222, 230]
# print(recBinarySearch(arr, 230, 0, len(arr)-1))