# Your task is to sum the differences between consecutive pairs in the array in descending order.

# Example
# [2, 1, 10]  -->  9
# In descending order: [10, 2, 1]

# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).

def sum_of_differences(arr):
    
    if len(arr) <= 1:
        return 0
    else:
        sum = 0
        arr.sort(reverse=True)
        for i in range(len(arr) - 1):
            iteration = arr[i] - arr[i+1] 
            sum += iteration
        return sum