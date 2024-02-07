def insertionSort(n, arr) -> list:  # Length of the array and the Array
    for i in range(1, n, 1): # (i = 1; i < n; i++)
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1           
        arr[j + 1] = key

    return arr