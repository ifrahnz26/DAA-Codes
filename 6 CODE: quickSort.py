'''In a database of numbers there is a table of unsorted numbers. 
The database admin now wants to sort these numbers using an approach 
where in the first element is selected as the pivot element for sorting. 
At certain point, the first half elements are less than the pivot and 
right half elements are greater than the pivot. 
Design and implement Quicksort algorithm to solve it. 
State the design strategy used and comment on the time complexity of the same.
'''
import time

def partition(A, l, r):
    p = A[l]  # pivot
    i = l
    j = r
    while True:
        while A[i] < p:
            i += 1
        while A[j] > p:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

def quicksort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quicksort(A, l, s)
        quicksort(A, s + 1, r)

A = list(map(int, input("Enter the elements: ").split()))

start = time.time()
quicksort(A, 0, len(A)-1)
end = time.time()

print("Sorted array: ", A)
print("Time taken: ", end - start)
