from typing import List
import unittest

# problem: Generate Parentheses
# @ https://leetcode.com/problems/generate-parentheses/
# author: Daniel Montilla (https://github.com/DanielMontilla)

def solution(n: int) -> List[str]:
  
  res: List[str] = []
  
  def traverse(stack: str, openCount: int, closeCount):
    
    if n == openCount == closeCount:
      res.append(stack)
      return
    
    if openCount < n:
      stack += '('
      traverse(stack, openCount + 1, closeCount)
      stack = stack[:-1]
    
    if closeCount < openCount:
      stack += ')'
      traverse(stack, openCount, closeCount + 1)
      stack = stack[:-1]
  
  
  traverse('(', 1, 0)
  
  return res

class Test(unittest.TestCase):
  def test_0(self):
    self.assertEqual(solution(3), ["((()))","(()())","(())()","()(())","()()()"])
  def test_1(self):
    self.assertEqual(solution(1), ["()"])
    
if __name__ == '__main__':
  unittest.main()
  
# Notes:
# Runtime: 65 ms, faster than 57.19% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.2 MB, less than 77.83% of Python3 online submissions for Generate Parentheses.