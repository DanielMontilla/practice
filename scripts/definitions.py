import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
PROBLEMS_DIR = os.path.join(ROOT_DIR, 'problems')

def DEF_RS_FILE(link: str = None):
  l = f'{link}' if link != None else '[TODO: place problem link here]'
  return (
"#![allow(dead_code)] \n"

f"\n// problem @ {l}\n"

"""
fn solution() -> Option<&'static str> {
    None
}

#[test]
fn test() {
    let a1 = None;
    assert_eq!(
      solution(), 
      None
    );
}

// Notes:
"""
  )
  
def DEF_PY_FILE(link: str = None):
  l = f'{link}' if link != None else '[TODO: place problem link here]'
  return (
"import unittest\n"

f"\n# problem @ {l}\n"

"""
def solution():
  return True

class Test(unittest.TestCase):
  def test(self):
    self.assertEqual(
      solution(),
      True
    )
    
if __name__ == '__main__':
  unittest.main()
"""
  )