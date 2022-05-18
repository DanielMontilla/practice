from typing import List

# https://leetcode.com/problems/product-of-array-except-self/
# COULD NOT SOLVE ON MY OWN. LOOKED ONLINE FOR HINT


def productExceptSelf(nums: List[int]) -> List[int]:
    l = len(nums)
    r = range(l)

    pre = [None] * l
    pos = [None] * l
    ans = [None] * l

    premult = 1
    posmult = 1

    for i in r:
        p = i - 1

        if p >= 0:
            premult *= nums[p]

        pre[i] = premult

    for i in reversed(r):
        p = i + 1

        if p < l:
            posmult *= nums[p]

        pos[i] = posmult

    for i in r:
        ans[i] = pre[i] * pos[i]

    return ans


"""
    Time: O(n) => time increases linearly
    Memory: O(n) => memory usage increase linearly too
    
    Runtime: 246 ms, faster than 81.59% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 22.3 MB, less than 23.89% of Python3 online submissions for Product of Array Except Self.
"""
