def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[i]:
                swap = arr[j]
                arr[j] = arr[i]
                arr[i] = swap
    return arr

mas = []
size = int(input("Введите размер массива:"))
for i in range(0, size):
    arr = int(input())
    mas.append(arr)
print(bubbleSort(mas))