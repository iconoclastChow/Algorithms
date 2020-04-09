"""
Find the base case and recursion case
Use word 'return' to recurse
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def recursion_sum(arr):
    print(arr)
    if not arr:
        return 0
    else:
        return arr[0] + recursion_sum(arr[1:])


if __name__ == '__main__':
    print(factorial(5))
    print(recursion_sum([3, 5, 7, 2, 7, 1, 5]))