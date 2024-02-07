def bubbleSort(n, arr) -> list: # Length of the array and the Array
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def optimizedBubbleSort(n, arr) -> list: # Length of the array and the Array
    for i in range(n-1):
        flag = True
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break

    return arr
