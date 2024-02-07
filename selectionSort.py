def selectionSort(arr, n) -> list: # Array and the length of the array
    for i in range(0, n - 1, 1): # i = 0; i < n - 1; i++
        min_idx = i
        
        for j in range(i + 1, n, 1): # j = i + 1; i < n; j ++
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr