"""
This is an implementation of the Insertion Sort algorithm
that sorts in monotonically decreasing order.
"""

"""
Instructions to run code:
1. Modify the array argument in the last line of code
2. Save the file and run the code using python3 <path>/InsertionSort.py
"""

def insertionSort(arr):
    l = len(arr)
    
    for i in range(1,l):
        key = arr[i]

        j = i-1
        while j>=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

print(insertionSort([3,5,1,6,7]))
            