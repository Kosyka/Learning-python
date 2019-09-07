def insertionSort(arr):
    for i in range(1, len(arr)):
        check = arr[i]
        j = i - 1
        while 0 <= j and check < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
        arr[j+1] = check
    return arr

mas = [53,12,5,11,34,7,78,141,0]

print(insertionSort(mas))