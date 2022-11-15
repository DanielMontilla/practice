#![allow(dead_code)] 

// problem @ [TODO: place problem link here]

use std::collections::HashMap;

fn solution(s: String) -> i32 {
  let mut max_count: i32 = 0;
  let mut start: i32 = -1;
  let mut record: HashMap<char, i32> = HashMap::new();

  for (i, c) in s.chars().enumerate() {
    let i = i as i32;
    match record.get(&c) {
      Some(position) => {
        // if there is  an entry in the map for this letter
        if position > &start {
          // if the current letter position is more than the current start
          start = *position;
        }

        // if the current letter's position less than the start (just update)
        record.insert(c, i);
      },
      None => { 
        // if letter doesn't exist in hashmap
        record.insert(c, i);
      }
    }

    // computing iteration count
    let count: i32 = i - start;

    if count > max_count { max_count = count };
  }

  return max_count;
}


#[test]
fn test_0() { assert_eq!(solution(String::from("abcabcbb")), 3) }
#[test]
fn test_1() { assert_eq!(solution(String::from("abcbrascba")), 5) }
#[test]
fn test_2() { assert_eq!(solution(String::from("bbbbb")), 1) }
#[test]
fn test_3() { assert_eq!(solution(String::from("pwwkew")), 3) }
#[test]
fn test_4() { assert_eq!(solution(String::from("a")), 1) }
#[test]
fn test_5() { assert_eq!(solution(String::from("")), 0) }


// Notes:
// Runtime: 7 ms, faster than 54.81% of Rust online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 2.1 MB, less than 76.62% of Rust online submissions for Longest Substring Without Repeating Characters.