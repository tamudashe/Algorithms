"""
Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.

"""


def max_sum_subarray(nums, k):
    window_start = 0
    max_sum = float('-inf')
    curr_sum = 0


    for window_end, num in enumerate(nums):
        curr_sum += num
        if window_end < k - 1:
            continue

        max_sum = max(max_sum, curr_sum)
        curr_sum -= nums[window_start]
        window_start += 1

    return max_sum


def main():
    nums1 = [2, 1, 5, 1, 3, 2]
    k1 = 3

    nums2 = [2, 3, 4, 1, 5]
    k2 = 2

    assert max_sum_subarray(nums1, k1) == 9
    assert max_sum_subarray(nums2, k2) == 7
    print("Passed all test cases!")


main()
