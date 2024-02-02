def mergeSort(arr, lo, hi) -> list:
    if lo == hi:
        return [arr[lo]]
        
    mid = (lo + hi) // 2

    left_half = mergeSort(arr, lo, mid)
    right_half = mergeSort(arr, mid + 1, hi)
    
    left_len = mid - lo + 1 
    right_len = hi - mid
    result = [None]*(left_len + right_len)

    i, j, k = 0, 0, 0

    while i < left_len and j < right_len:
        if left_half[i] < right_half[j]:
            result[k] = left_half[i]
            i += 1
            k += 1
        else:
            result[k] = right_half[j]
            j += 1
            k += 1

    while i < left_len:
        result[k] = left_half[i]
        i += 1
        k += 1

    while j < right_len:
            result[k] = right_half[j]
            j += 1
            k += 1        
        
    return result