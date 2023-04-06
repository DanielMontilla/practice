import { assertEquals } from "https://deno.land/std@0.182.0/testing/asserts.ts";
const { test } = Deno;

/** 
 * problem: Reverse Linked List
 * @ https://leetcode.com/problems/reverse-linked-list/
 * author: Daniel Montilla (https://github.com/DanielMontilla)
 */


/**
 * Definition for singly-linked list.
*/
class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function solution(head: ListNode | null): ListNode | null {

  if (head === null) return null;

  let a = head;
  let b = head.next;

  while (b !== null) {
    const temp = b.next;

    b.next = a;

    a = b;
    b = temp;
  }

  head.next = null;

  return a;
}

function createLinkedList(nums: number[]): ListNode | null {
  if (nums.length === 0) {
    return null;
  }
  const head = new ListNode(nums[0]);
  let current = head;
  for (let i = 1; i < nums.length; i++) {
    const newNode = new ListNode(nums[i]);
    current.next = newNode;
    current = newNode;
  }
  return head;
}


test('test_0', () => {
  const list = [1,2,3,4,5];
  const head = createLinkedList(list);
  const expected = createLinkedList(list.toReversed());
  assertEquals(solution(head), expected);
});
test('test_1', () => {
  const list = [1,2];
  const head = createLinkedList(list);
  const expected = createLinkedList(list.toReversed());
  assertEquals(solution(head), expected);
});
test('test_3', () => {
  const list: number[] = [];
  const head = createLinkedList(list);
  const expected = createLinkedList(list.toReversed());
  assertEquals(solution(head), expected);
});

/** Notes:
 * Runtime 66 ms Beats 75.7%
 * Memory 44.3 MB Beats 97.24%
 */