def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1
def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)
data = [8, 7, 2, 1, 0, 9, 6]
print("The unsorted list is: ")
print(data)
size = len(data)
quicksort(data, 0, size - 1)
print("The sorted array is: ")
print(data)
