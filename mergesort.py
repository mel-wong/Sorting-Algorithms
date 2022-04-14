# Merge Sort
# Algorithm: Divide and conquer where the list is split in half.
# each sub-list is sorted and then merged back together

def merge_sort(array):

    # only splits array if more than 1 element
    if len(array) > 1:

        # split array in half
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]

        # keep pointers to new left and right arrays and original array
        l_index = 0
        r_index = 0
        arr_index = 0

        merge_sort(left)
        merge_sort(right)

        while l_index < len(left) and r_index < len(right):

            if left[l_index] < right[r_index]:
                array[arr_index] = left[l_index]
                l_index += 1

            else:
                array[arr_index] = right[r_index]
                r_index += 1

            arr_index += 1

        # checks if any other elements not yet placed
        while l_index < len(left):
            array[arr_index] = left[l_index]
            arr_index += 1
            l_index += 1

        while r_index < len(right):
            array[arr_index] = right[r_index]
            arr_index += 1
            r_index += 1










