"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""
def average_contiguous_array(nums, k):
    averages = []
    window_start = 0

    curr_average = 0

    for window_end, num in enumerate(nums):
        curr_average += num

        if window_end < k - 1:
            continue

        averages.append(curr_average/k)
        curr_average -= nums[window_start]
        window_start += 1

    return averages

def main():
    test = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5

    print(average_contiguous_array(test, k))


main()
