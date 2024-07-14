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
    p = A[l]  # Selecting the first element as pivot
    i = l     # Left pointer starting at the beginning of the array
    j = r     # Right pointer starting at the end of the array
    
    while True:
        # Move the left pointer to the right until finding an element greater than or equal to the pivot
        while A[i] < p:
            i += 1
        
        # Move the right pointer to the left until finding an element less than or equal to the pivot
        while A[j] > p:
            j -= 1
        
        # If the left pointer is greater than or equal to the right pointer, break the loop
        if i >= j:
            return j
        
        # Swap the elements at the left and right pointers
        A[i], A[j] = A[j], A[i]
        
        # Move both pointers towards the center
        i += 1
        j -= 1

def quicksort(A, l, r):
    if l < r:
        # Partition the array into two parts using the partition function
        s = partition(A, l, r)
        
        # Recursively sort the left and right parts
        quicksort(A, l, s)     # Sort the left part
        quicksort(A, s + 1, r) # Sort the right part

# Input array from user
A = list(map(int, input("Enter the elements: ").split()))

# Measure the start time of the sorting process
start = time.time()

# Sort the array using quicksort algorithm
quicksort(A, 0, len(A) - 1)

# Measure the end time of the sorting process
end = time.time()

# Print the sorted array and the time taken for sorting
print("Sorted array: ", A)
print("Time taken: ", end - start)
