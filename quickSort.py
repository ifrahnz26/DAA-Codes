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
    j = r + 1  # initialize j to r + 1, as per the given constraint
    
    while i < j:
        while A[i] < p:
            i += 1
        while A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    
    # Swap pivot with A[j] to put the pivot in its correct place
    A[l], A[j] = A[j], A[l]
    return j

def quicksort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quicksort(A, l, s - 1)
        quicksort(A, s + 1, r)

n = int(input("Enter the number of elements: "))
A = list(map(int, input("Enter the elements (space-separated): ").split()))

# Append infinity value as sentinel
A.append(float('inf'))
start = time.time()
quicksort(A, 0, n - 1)
end = time.time()
# Remove the sentinel value
A.pop()
print("Sorted array: ", A)
print("Time taken: ", end - start)
