"""
Questions:
Two Sums
"""


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

arr = [2, 3, 7, 11, 34]
target = 9
print(two_sum(arr, target))