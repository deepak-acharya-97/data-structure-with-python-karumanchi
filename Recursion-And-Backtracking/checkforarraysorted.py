def isArraySorted(arr,startIndex, endIndex):
    if(startIndex == endIndex-1):
        return True
    return arr[startIndex] <= arr[startIndex+1] and isArraySorted(arr, startIndex+1, endIndex)

print isArraySorted([1,2,10,9],0,4)