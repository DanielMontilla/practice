import re
import unittest

# problem @ [TODO: place problem link here]

def solution(s: str) -> bool:
  # first convert string
  s = re.sub('[^A-Za-z0-9]+', '', s).lower()

  length = len(s)

  l = 0
  r = length - 1

  length = (length // 2)

  for i in range(length):
      if s[l] != s[r]:
          return False

      l += 1
      r -= 1

  return True

class Test(unittest.TestCase):
  def test_0(self):
    self.assertEqual(
      solution("A man, a plan, a canal: Panama"),
      True
    )
  def test_1(self):
    self.assertEqual(
      solution("race a car"),
      False
    )
  def test_2(self):
    self.assertEqual(
      solution(" "),
      True
    )
    
if __name__ == '__main__':
  unittest.main()