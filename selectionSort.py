def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == '__main__':
    arr = [2, 1, 6, 3, 7, 3, 5, 0, 1]
    arr_sorted = selection_sort(arr)
    print(arr_sorted)
