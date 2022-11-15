from typing import List
import unittest

# problem @ [TODO: place problem link here]

def solution_1(numbers: List[int], target: int) -> List[int]:
  for i in range(len(numbers)):
    for j in range(len(numbers) - i):
      i1 = i
      i2 = i + j
      if numbers[i1] + numbers[i2] == target and i1 != i2:
        return [i1 + 1, i2 + 1]

def solution(numbers: List[int], target: int) -> List[int]:
  l = 0
  r = len(numbers) - 1

  while numbers[l] + numbers[r] != target:
    if numbers[l] + numbers[r] > target:
      r -= 1
    else:
      l += 1

  return [l + 1, r + 1]

class Test(unittest.TestCase):
  def test_0(self):
    self.assertEqual(
      solution([2,7,11,15], 9),
      [0,1]
    )
  def test_1(self):
    self.assertEqual(
      solution([3,2,4], 6),
      [1, 2]
    )
  def test_2(self):
    self.assertEqual(
      solution([-1,0], -1),
      [0, 1]
    )
    
if __name__ == '__main__':
  unittest.main()
  
# Notes:
