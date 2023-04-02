#![allow(dead_code)]

/// problem: Search a 2D Matrix
/// @ https://leetcode.com/problems/search-a-2d-matrix/
/// author: Daniel Montilla (https://github.com/DanielMontilla)

fn solution(matrix: Vec<Vec<i32>>, target: i32) -> bool {
   let mut left = 0;
   let mut right = matrix.len() - 1;
   let mut row = 0;

    while left <= right {
        let mid = (left + right) / 2;

        let first = matrix[mid].first().unwrap();
        let last = matrix[mid].last().unwrap();

        if first <= &target && last >= &target {
            row = mid;
            break;
        } else if &target > last {
            left = mid + 1;
        } else {
            if mid <= 0 { break; }
            right = mid - 1;
        }
    }

    let arr = &matrix[row];
    left = 0;
    right = arr.len() - 1;

    while left <= right {
        let mid = (left + right) / 2;

        if arr[mid] == target {
            return true
        } else if arr[mid] < target {
            left = mid + 1;
        } else {
            if mid <= 0 { break; }
            right = mid - 1;
        }
    }

   return false;
}

#[test]
fn test_0() {
    let matrix: Vec<Vec<i32>> = vec![
        vec![1,3,5,7],
        vec![10,11,16,20],
        vec![23,30,34,60]
    ];
    assert_eq!(solution(matrix, 3), true)
}
#[test]
fn test_1() {
    let matrix: Vec<Vec<i32>> = vec![
        vec![1,3,5,7],
        vec![10,11,16,20],
        vec![23,30,34,60]
    ];
    assert_eq!(solution(matrix, 13), false)
}
#[test]
fn test_2() {
    let matrix: Vec<Vec<i32>> = vec![
        vec![1]
    ];
    assert_eq!(solution(matrix, 0), false)
}
#[test]
fn test_3() {
    let matrix: Vec<Vec<i32>> = vec![
        vec![1,3,5,7],
        vec![10,11,16,20],
        vec![23,30,34,50]
    ];
    assert_eq!(solution(matrix, 10), true)
}

// Notes:
