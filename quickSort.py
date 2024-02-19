def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p-1)
        quickSort(arr, p+1, hi)


def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo

    for j in range(i+1, hi+1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[lo] = arr[lo], arr[i]
    return i