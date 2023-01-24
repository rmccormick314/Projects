import numpy as np
import time

def swap_elements(array, position_one, position_two):
    temp_holder = array[position_one]

    array[position_one] = array[position_two]
    array[position_two] = temp_holder

def insertion_sort(array):
    i = 1;

    while (i < len(array)):
        key = array[i]
        j = i - 1

        while (j >= 0 and key < array[j]):
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key
        i += 1

def selection_sort(array):
    i = 0
    while (i < len(array)):
        minimum_index = i
        j = i + 1
        while (j < len(array)):
            if (array[minimum_index] > array[j]):
                minimum_index = j
            j += 1

        swap_elements(array, i, minimum_index)
        i += 1

def merge_sort(array):
    if (len(array) > 1):
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while (i < len(left) and j < len(right)):
            if (left[i] < right[j]):
                array[k] = left[i]
                i += 1
            else:
                array[k] = left[i]
                j += 1
            k += 1

        while (i < len(left)):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if(start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end

def quick_sort(array):
    quick_sort_helper(array, 0, len(array)-1)

def quick_sort_helper(array, start, end):
    if (start < end):
        partition_index = partition(array, start, end)

        quick_sort_helper(array, start, partition_index - 1)
        quick_sort_helper(array, partition_index+1, end)

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if (array[j] > array[j+1]):
                swap_elements(array, j+1, j)

def array_order_test(array):
    in_order = True
    i = 0
    while (i < len(array) - 1):
        if (array[i] > array[i+1]):
            return False
        i += 1
    return in_order

def test_sorts():
    sorting_methods = [insertion_sort, selection_sort, merge_sort, quick_sort, bubble_sort]

    items_per_array = 25000

    print()
    print("Testing sorts with " + str(items_per_array) + " size arrays.")
    print()

    x = 0
    while (x < len(sorting_methods)):
        test_array = np.random.randint(1, 100, items_per_array)

        start_time = time.time()
        sorting_methods[x](test_array)
        end_time = time.time()

        total_time = end_time - start_time

        if (array_order_test(test_array)):
            print(str(sorting_methods[x]) + " PASSED in " + str(total_time))
        else:
            print(str(sorting_methods[x]) + " FAILED")

        x += 1

    print()
    print("Testing completed.")

if __name__ == "__main__":
    test_sorts()
