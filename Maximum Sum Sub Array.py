def maxSumsub(arr, lo, hi):
    if lo == hi:
        return arr[lo]
    
    if lo > hi:
        return float("-inf")
    mid = (lo+hi)//2

    lss = maxSumsub(arr, lo, mid-1)
    rss = maxSumsub(arr, mid+1, hi)
    css = crossSum(arr, lo, mid, hi)

    return max(lss, css, rss)

def crossSum (arr, lo, mid, hi):
    leftSum = 0
    maxLeftSum = float("-inf")
    for i in range(mid, lo-1, -1):
        leftSum += arr[i]
        maxLeftSum = max(leftSum, maxLeftSum)
    
    rightSum = 0
    maxRightSum = float("-inf")
    for j in range(mid, hi+1, 1):
        rightSum += arr[j]
        maxRightSum = max(rightSum, maxRightSum)

    return maxLeftSum + maxRightSum - arr[mid]


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSumsub(arr, 0, len(arr)-1)) # arr, 0, 8