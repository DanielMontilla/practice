#![allow(dead_code)] 

// problem @ https://leetcode.com/problems/container-with-most-water/

fn solution(height: Vec<i32>) -> i32 {
  let mut max_area = 0;
  let mut l = 0;
  let mut r = height.len() - 1;

  let mut check_area = |width: usize, height: usize| {
    let area = width * height; // computing area
    if area > max_area { max_area = area } // checking if it's more than current max
  };

  loop {
    if l >= r { break }

    let lval = height[l];
    let rval = height[r];

    let width = r - l;

    if lval <= rval {
      check_area(width, lval as usize);
      while height[l] <= lval { // moving left pointer right
        l += 1 ;
        if l >= r { break };
      }
    } else {
      check_area(width, rval as usize);
      while height[r] <= rval { // moving right pointer left
        r -= 1;
        if r <= l { break };
      }
    }
  }

  return max_area as i32;
}

#[test]
fn test_0() { assert_eq!(solution(vec![1,8,6,2,5,4,8,3,7]), 49) }
#[test]
fn test_1() { assert_eq!(solution(vec![1,1]), 1); }

// Notes:
// Runtime: 16 ms, faster than 51.89% of Rust online submissions for Container With Most Water.
// Memory Usage: 2.9 MB, less than 66.98% of Rust online submissions for Container With Most Water.