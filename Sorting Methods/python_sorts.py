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

def test_sorts():
    array = [6, 3, 1, 2, 4, 5, 12, 69, 420, 7]
    print("Base Array:")
    print(array)
    print()

    test_array_insertion = array
    insertion_sort(test_array_insertion)
    print("Insertion Sort:")
    print(test_array_insertion)
    print()

    test_array_selection = array
    selection_sort(test_array_selection)
    print("Selection Sort:")
    print(test_array_selection)
    print()

    test_array_merge = array
    merge_sort(test_array_merge)
    print("Merge Sort:")
    print(test_array_merge)
    print()

test_sorts()
