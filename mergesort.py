import time

def mergesort(arr, low, high):
    # Base case: if the segment size is greater than 1
    if high - low + 1 > 1:
        mid = (low + high) // 2  # Find the middle point
        mergesort(arr, low, mid)  # Recursively sort the first half
        mergesort(arr, mid + 1, high)  # Recursively sort the second half
        merge(arr, low, mid, high)  # Merge the two halves

def merge(arr, low, mid, high):
    b = []  # Temporary array to store the merged result
    h = low  # Starting index for the left half
    j = mid + 1  # Starting index for the right half

    # Merge the two halves into the temporary array b[]
    while h <= mid and j <= high:
        if arr[h] <= arr[j]:
            b.append(arr[h])
            h += 1
        else:
            b.append(arr[j])
            j += 1

    # Copy any remaining elements of the left half
    while h <= mid:
        b.append(arr[h])
        h += 1

    # Copy any remaining elements of the right half
    while j <= high:
        b.append(arr[j])
        j += 1

    # Copy the merged elements back into the original array
    for k in range(low, high + 1):
        arr[k] = b[k - low]

# Input the array elements
arr = list(map(int, input("Enter the elements: ").split()))

# Record the start time
start = time.time()

# Perform merge sort
mergesort(arr, 0, len(arr) - 1)

# Record the end time
end = time.time()

# Print the sorted array and time taken
print("Sorted array: ", arr)
print("Time taken: ", end - start)
