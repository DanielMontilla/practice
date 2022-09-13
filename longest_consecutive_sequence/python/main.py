from typing import List

# https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums: List[int]) -> int:
    hashset = set(nums)

    longest = 0

    for i in range(len(nums)):
        n = nums[i]
        current = 0

        if n - 1 not in hashset:
            while n in hashset:
                current += 1
                n += 1
            if current > longest:
                longest = current

    return longest


# Notes:
""""
    Runtime: 2185 ms, faster than 28.95% of Python3 online submissions for Longest Consecutive Sequence.
    Memory Usage: 28.6 MB, less than 20.03% of Python3 online submissions for Longest Consecutive Sequence.

    pretty bad results. more time required for optimized solution
"""

# Inputs:
nums_1 = [100,4,200,1,3,2]
nums_2 = [0,3,7,2,5,8,4,6,0,1]

if __name__ == '__main__':
    res = longestConsecutive(nums_1)
    print(res)