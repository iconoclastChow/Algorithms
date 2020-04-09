def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        arr_less = [i for i in arr[1:] if i <= pivot]
        arr_more = [i for i in arr[1:] if i > pivot]
        return quick_sort(arr_less) + [pivot] + quick_sort(arr_more)
        # transform pivot(single value) into list


if __name__ == '__main__':
    print(quick_sort([4, 7, 2, 9, 1, 0, 4]))