# Quick Sort
# Algorithm: Divide and conquer sorting method
# Picks right-most element as the pivot and partitions array around the pivot element

# Method to find the partition index
def partition(array, low, high):
    # Make the right most element the pivot element
    pivot = array[high]

    # pointer for right most element below pivot value
    i = low - 1

    # Traverse through array to find all elements below pivot value
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            # swap the two elements such that the element lower than the pivot is on left side
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    # swap the pivot element with the element just after pointer i
    array[high] = array[i + 1]
    array[i + 1] = pivot

    # return position of pivot element
    return i + 1


# Quicksort method that uses partition method to sort array
def quick_sort(array, low, high):

    if low < high:
        # find the pivot index where left elements are all less than pivot element
        pivot_index = partition(array, low, high)

        # Recursively call for elements to the left of the pivot
        quick_sort(array, low, pivot_index - 1)

        # Recursively call for elements to the right of the pivot
        quick_sort(array, pivot_index + 1, high)
