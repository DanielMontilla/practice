from typing import List
import unittest

# problem @ https://leetcode.com/problems/top-k-frequent-elements/

def solution(nums: List[int], k: int) -> List[int]:

  counts = dict()
  res = []

  for n in nums:
      counts[n] = counts.get(n, 0) + 1

  def findMax():
    m = None
    for n in counts:
      if m == None or counts[n] > counts[m]:
        m = n

    return m

  for i in range(k):
    n = findMax()
    res.append(n)
    counts.pop(n)

  return res

class Test(unittest.TestCase):
  def test_0(self):
    self.assertEqual(
      solution([1,1,1,2,2,3], 2),
      [1,2]
    )
  def test_1(self):
    self.assertEqual(
      solution([1], 1),
      [1]
    )
    
if __name__ == '__main__':
  unittest.main()
  
# Notes:
"""
  Time complexity: O(n * k) ?
  Space complexity: O(n + k) ?
  
  Runtime: 355 ms, faster than 5.02% of Python3 online submissions for Top K Frequent Elements.
  Memory Usage: 18.5 MB, less than 90.85% of Python3 online submissions for Top K Frequent Elements.

  would like to try another approach to decrease time complexity
"""