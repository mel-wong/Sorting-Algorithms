# Optimized Bubble Sort
# Algorithm: Comparison sort where adjacent elements are compared
# The largest element gets placed at the end of list by the end of each pass-through
# Knows list is sorted when no swaps have occurred in single pass-through

def bubble_sort(array):

	length = len(array)

	for i in range(length):

		# swapped variable to track if an element has been swapped during passthrough
		swapped = False

		for j in range(0, length-i-1):

			if array[j] > array[j + 1]:
				swap_val = array[j]
				array[j] = array[j + 1]
				array[j + 1] = swap_val
				swapped = True

		if not swapped:
			break
