#![allow(dead_code)]

/// problem: Min Stack
/// @ https://leetcode.com/problems/min-stack/
/// author: Daniel Montilla (https://github.com/DanielMontilla)

struct MinStack {
  main_stack: Vec<i32>,
  index_stack: Vec<usize>
}

impl MinStack {

  fn new() -> Self {
    MinStack { main_stack: vec![], index_stack: vec![] }
  }
  
  fn push(&mut self, val: i32) {
    let j = self.main_stack.len();
    self.main_stack.push(i32::clone(&val));

    match self.index_stack.last() {
      Some(i) => {
        match self.main_stack.get(*i) {
          Some(v) => {
            if val <= *v {
              self.index_stack.push(j);
            }
          },
          None => panic!("how")
        }
      },
      None => self.index_stack.push(j)
    }
  }
  
  fn pop(&mut self) {
    self.main_stack.pop();

    match self.index_stack.last() {
      Some(i) => {
        if *i == self.main_stack.len() {
          self.index_stack.pop();
        }
      },
      None => panic!("can't call `pop` on an empty stack")
    }
  }
  
  fn top(&self) -> i32 {
    match self.main_stack.last() {
      Some(v) => *v,
      None => panic!("can't call `top` on an empty stack")
    }
  }
  
  fn get_min(&self) -> i32 {
    match self.index_stack.last() {
      Some(i) => {
        match self.main_stack.get(*i) {
          Some(v) => *v,
          None => panic!("how")
        }
      },
      None => panic!("can't call `top` on an empty stack")
    }
  }
}

#[test]
fn test_0() {
  let mut min_stack = MinStack::new();
  min_stack.push(-2);
  min_stack.push(0);
  min_stack.push(-3);

  assert_eq!(min_stack.get_min(), -3);
  min_stack.pop();
  assert_eq!(min_stack.top(), 0);
  assert_eq!(min_stack.get_min(), -2);
}
#[test]
fn test_1() {
  let mut min_stack = MinStack::new();
  min_stack.push(10);
  min_stack.push(5);
  min_stack.push(5);
  min_stack.push(9);
  min_stack.push(4);
  assert_eq!(min_stack.get_min(), 4);
  for _ in 0..3 { min_stack.pop() }
  assert_eq!(min_stack.get_min(), 5);
  min_stack.push(2);
  min_stack.push(100);
  assert_eq!(min_stack.top(), 100);
  for _ in 0..2 { min_stack.pop() }
  min_stack.push(6);
  assert_eq!(min_stack.get_min(), 5);
}

// Notes:
// Runtime: 11 ms, faster than 42.37% of Rust online submissions for Min Stack.
// Memory Usage: 6.1 MB, less than 16.10% of Rust online submissions for Min Stack.

// honesrtly pretty bad. could probably improve speed by using std's stack data structure