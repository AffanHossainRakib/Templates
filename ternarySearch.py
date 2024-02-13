def TernarySearch(arr, key, lo, hi) -> int: # iterative

    while lo <= hi:
        mid1 = lo + (hi-lo)//3
        mid2 = hi - (hi-lo)//3

        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        else:
            if key < arr[mid1]:
                hi = mid1 - 1
            elif arr[mid2] < key:
                lo = mid2 + 1
            else:
                lo = mid1 + 1
                hi = mid2 - 1
                
    return -1

def recTerSearch(arr, key, lo, hi) -> int: # recursive
    if lo > hi:
        return -1
    
    mid1 = lo + (hi-lo)//3
    mid2 = hi - (hi-lo)//3

    if arr[mid1] == key:
        return mid1
    elif arr[mid2] == key:
        return mid2
    else:
        if key < arr[mid1]:
            return recTerSearch(arr, key, lo, mid1-1)
        elif arr[mid2] < key:
            return recTerSearch(arr, key, mid2+1, hi)
        else:
            return recTerSearch(arr, key, mid1+1, mid2-1)



# arr = [1, 2, 4, 5, 7, 8, 20, 20, 221, 222, 230]
# print(TernarySearch(arr, 230, 0, len(arr)-1))