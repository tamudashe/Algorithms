"""
Question:
    Write a function that returns a permutation of a given list.

Input:

Output:

"""

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def solution(nums, low, high, result):
    if low == high:
        result.append(nums)

    for i in range(low, high + 1):
        swap(nums, low, i)
        solution(nums, low + 1, high, result)
        swap(nums, low, i)


def permute(arr):
    l = len(arr)
    result = []
    solution(arr, 0, l - 1, result)
    return result


def main():
    nums = [1, 2, 3]
    print(permute(nums))


if __name__ == '__main__':
    main()
