#![allow(dead_code)]

/// problem: Binary Search
/// @ https://leetcode.com/problems/binary-search/
/// author: Daniel Montilla (https://github.com/DanielMontilla)


fn solution(nums: Vec<i32>, target: i32) -> i32 {
  let mut l: usize = 0;
  let mut r: usize = nums.len();

  if target < nums[l] || target > nums[r - 1] { return -1 }

  loop {
    let m = l + ( (r - l) / 2 );
    if target == nums[m] { return m as i32 }
    if target < nums[m] {
      r = m;
      // when we move r; check if r & l overlap
      if r == l { break }
    } else {
      l = m;
      // when we move l; check if r & l are touching
      if r == l + 1 { break }
    }
  }

  return -1
}

#[test]
fn test_0() { assert_eq!(solution(vec![-1,0,3,5,9,12], 9), 4) }
#[test]
fn test_1() { assert_eq!(solution(vec![-1,0,3,5,9,12], 2), -1) }
#[test]
fn test_2() { assert_eq!(solution(vec![-1,0,3,5,9,12], 12), 5) }
#[test]
fn test_3() { assert_eq!(solution(vec![1], 1), 0) }
#[test]
fn test_4() { assert_eq!(solution(vec![1], 0), -1) }
#[test]
fn test_5() { assert_eq!(solution(vec![-1,0,5], 0), 1) }
#[test]
fn test_6() { assert_eq!(solution(vec![0], 0), 0) }
#[test]
fn test_7() { assert_eq!(solution(vec![0], 100), -1) }

// Notes:
// Runtime 5 ms Beats 78.47%
// Memory 2.2 MB Beats 78.65%