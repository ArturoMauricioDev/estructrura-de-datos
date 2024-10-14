def bubleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
    return arr


print(bubleSort([5, 2, 7, 3, 1, 8, 2, 6, 9]))
