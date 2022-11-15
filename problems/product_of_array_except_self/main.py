from typing import List
import unittest

# problem @ https://leetcode.com/problems/product-of-array-except-self/

def solution(nums: List[int]) -> List[int]:
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

class Test(unittest.TestCase):
  def test_0(self):
    self.assertEqual(
      solution([1,2,3,4]),
      [24,12,8,6]
    )
  def test_1(self):
    self.assertEqual(
      solution([-1,1,0,-3,3]),
      [0,0,9,0,0]
    )
    
if __name__ == '__main__':
  unittest.main()
  
# Notes:
"""
  Time: O(n) => time increases linearly
  Memory: O(n) => memory usage increases linearly too
  
  Runtime: 246 ms, faster than 81.59% of Python3 online submissions for Product of Array Except Self.
  Memory Usage: 22.3 MB, less than 23.89% of Python3 online submissions for Product of Array Except Self.
"""