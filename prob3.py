def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
arr = list(map(int ,input().split()))
insertionSort(arr)
lst = [] 
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i]) 
print(lst)