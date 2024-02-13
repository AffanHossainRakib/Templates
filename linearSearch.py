def LinSearch(arr, key) -> int: # iterative
    for idx in range(len(arr)):
        if arr[idx] == key:
            return idx
    return -1

def RecLinSearch(arr, key, idx=0) -> int: # recursive
    if idx >= len(arr):
        return -1
    if arr[idx] == key:
        return idx
    return RecLinSearch(arr, key, idx+1)

# arr = [1, 2, 4, 5, 7, 8, 20, 20, 221, 222, 230]
# print(linSearch(arr, 500))