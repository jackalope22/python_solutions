def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break
    print(arr)

lista = [3,5,9,4,6,7,8,10,2,1,89,4,5,32,1,4,7,1,56,41,44,55,97,23,35,62,12,31]

bubbleSort(lista)